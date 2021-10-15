

function check_pass()
{
	if ( document.getElementById('id_password2').value != document.getElementById('id_password1').value ){
		document.getElementById('msg').style.color = 'red';
		document.getElementById('msg').innerHTML = 'Zadeli jste jiná hesla!';
	}
}