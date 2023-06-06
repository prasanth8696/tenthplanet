public class User {

	private String username = "";
	private String bankname = "";

	public User(){
	
	
	}
	public User(String username,String bankname){
		this.username = username;
		this.bankname = bankname;
	
	}

	public String getUserName(){
		return this.username;
	}
	public void setUserName(String username){
		this.username = username;
	}

	public String getBankName(){
                return this.bankname;
        }
        public void setBankName(String bankname){
                this.bankname = bankname;
       }

       @Override
       public boolean equals(Object ob){
		if (ob == this)
			return true;
		if (!(ob instanceof User)) 
         		return false;

	        User user = (User) ob;
		return this.username.equals(user.username); 

	}




}
