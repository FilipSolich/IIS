

function check_pass()
{
	if ( document.getElementById('id_password2').value != document.getElementById('id_password1').value ){
		document.getElementById('msg').style.color = 'red';
		document.getElementById('msg').innerHTML = 'Zadeli jste jiná hesla!';
		document.getElementById('msg').style.display = 'block';
		document.getElementById('submit').style.display = 'none';
	}
	else{
		document.getElementById('msg').style.display = 'none';
		document.getElementById('submit').style.display = 'block';
	}
}