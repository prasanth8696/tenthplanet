/*
 * 
 * https://medium.com/geekculture/how-to-implement-user-authentication-using-jwt-json-web-token-in-nodejs-and-maintain-user-c5850aed8839

fetch('https://reqres.in/api/users/1').then(
 (res) => {res.json()}).then((data) => {console.log(data)}) */



let a = 10;

let b = 10;



document.getElementById("btn").addEventListener('click',load);



function load(){


	const xhttp = new XMLHttpRequest();


	xhttp.onload = function(){
		if (this.status == 200){
		let values = JSON.parse(this.responseText);
		console.log(values[0]);
		console.log(values[2]);
		var output="";
		let i = 0;
		while(i < 25){
		output += '<div class="row">' + 
			   '<div class="col-4 float-left">' +
			     `<img src="${values[i].logo}" width="60" height="60">` +
			      `<ui>` +
			      `<li>${values[i].name} </li>` +
			      `<li>${values[i].country}</li>` +
			    '</div>' +
			    '<div class="col-4 float-none">' +
                             `<img src="${values[i+1].logo}" width="60" height="60">` +
                              `<ui>` +
                              `<li>${values[i+1].name} </li>` +
                              `<li>${values[i+1].country}</li>` +
                            '</div>' +
			     '<div class="col-4 float-right">' +
                             `<img src="${values[(i+2)].logo}" width="60" height="60">` +
                              `<ui>` +
                              `<li>${values[i+2].name} </li>` +
                              `<li>${values[i+2].country}</li>` +
                            '</div>' +
			   '</div>'
		i += 3;
		}
		document.getElementById("list").innerHTML = output





		}
	}

		xhttp.open('GET','https://api.instantwebtools.net/v1/airlines',true);
		xhttp.send();

}


