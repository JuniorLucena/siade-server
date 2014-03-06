function loadPage(link){
	$(".content").load(link);
	return false;
}

function sendForm(form){
	var url = form.action;
	$.ajax({
		type:'POST',
		data:$(form).serialize(),
		url: url,
		success:function(data,textStatus){
			jQuery('#content').html(data);
		},
		error:function(XMLHttpRequest,textStatus,errorThrown){}

	});	
	return false;
}



function sendFormModal(form){
	var url = form.action;
	$.ajax({
		type:'POST',
		data:$(form).serialize(),
		url: url,
		success:function(data,textStatus){
			$('#myModalLocation').modal('hide');
			alert("dados salvos");
		}
	});	
	return false;
}

//metodo responsavel por buscar as cidades de um estado, e atribuir os valores na lista de localizacao nas configuracoes.
function selectedState() {
	var myselect = document.getElementById("state.id")
	var dados = {'idState': myselect.options[myselect.selectedIndex].value}
	
	$.ajax({
		dataType: "json",
		type:'POST',
		data: dados,
		url: "/siade-server/settings/getCitiesByStateId",
		success: function(data, textStatus) {
			$('.settingsCity').html('')
			$.each( data, function( key, value ) {
				$('.settingsCity').append('<option value="' + value.id + '">'+ value.name + '</option>')
			});
		}
	});
}
			