


//jquery get and set methods


$(document).ready(function(){
    $('button').click(function() {

	var text = $('P').text();
	console.log(text);
	$('h1').text('fucking tutorial')
	//$('ul').append(`<li>${text}</li>`);
	});
});



$(document).ready(function() {
	$('#btn').click(function(){
	var val = $('#test').val();
        console.log(val);

  	$('#test').val('master shan')
       });


})


//fetch('https://dummy.restapiexample.com/api/v1/employees').then((response) => response.json()).then((data) => console.log(data)	)

/*
fetch('https://dummy.restapiexample.com/api/v1/create',{
  method : "POST",
  headers : {'Content-Type' : 'application/json'},
  body: JSON.stringify({name : "ayyapan",salary:"25000","age" : "25"})
}
).then((res) => res.json()).then((data) => console.log(data)).catch((e) => console.log(e))

console.log(document.getElementById('test').value)

*/

/*

fetch('https://dummy.restapiexample.com/api/v1/update/3103',{
 method : "UPDATE",

 headers : {'Content-Type' : 'application/json'},

 body : JSON.stringify({"name" : "shan",'salary' : "2000","age" : "20"})
 }

).then((res) => res.json()).then((data) => console.log(data))

*/


fetch('http://127.0.0.1:8000/login',{
method : "POST"
}).then(res => res.json()).then(data => console.log(data)).catch( (e) => console.log.data)
