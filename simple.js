


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





console.log(document.getElementById('test').value)
