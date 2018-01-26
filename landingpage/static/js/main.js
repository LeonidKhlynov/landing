window.onload = function(){
	document.getElementById('toggler').onclick = function(){
		show_notif('notif', this);
	}
}


function show_notif(id, toggler) {
	var notif = document.getElementById(id);
	var fio = document.getElementById('id_fio');
		if (notif.style.display == 'block') {
			notif.style.display = 'none';
		}else{
			notif.style.display = 'block';
		}

}