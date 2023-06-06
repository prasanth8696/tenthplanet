import secrets
from fastapi import FastAPI,Request,HTTPException
from datetime import datetime,timedelta
from starlette.middleware.sessions import SessionMiddleware
from fastapi.middleware.cors import CORSMiddleware
from database import session,Base,SessionData,engine

Base.metadata.create_all(bind=engine)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.add_middleware(
    SessionMiddleware,
    secret_key="my-secret-key",
    session_cookie="session_id",
    max_age=3600,  # 1 hour
)


@app.middleware("http")
async def validate(request: Request,call_next) :
    session = request.cookies.get('session_id',None)
    response = await call_next(request)
    print(session)

    if session :
        response.set_cookie(key="session_id",value=session,httponly=True)
    return response


def create_session(user_id) :
  session_id = secrets.token_hex(16)
  new_session = SessionData(
	id=session_id,
        is_loggedIn = True,
        user_id = user_id,
        expire_time = datetime.now() + timedelta(minutes=30)
  )

  session.add(new_session)
  session.commit()


def validate_session(session_id) :
  print(session_id)
  ses = session.query(SessionData).filter(SessionData.id == session_id.strip()).first()
  print(ses)

  if not ses :
    raise HTTPException(status_code=402,detail="Un authorized")

  if datetime.now() > ses.expire_time :
     session.delete(ses)
     session.commit()
     raise HTTPException(status_code=401,detail="Forbidden")
  else :
   return True

@app.get('/login')
async def login(request: Request) :
    create_session("shan")

    return {"msg" : "successfully logged in", "status_code" : 200}


@app.get('/get_page')
async def page(request : Request) :
   if validate_session(request.cookies.get("session_id",None)) :
        return {"msg" : "add sample page","status_code" : 200}



@app.get('/log_out')
async def logout(request : Request) :
   session_id = request.cookies.get("session_id",None)
   ses = session.query(SessionData).filter(SessionData.id == session_id).first()
   if ses :
    session.delete(ses)
    session.commit()

   return {"msg" : "successfully logged out","status_code" : 200 }




