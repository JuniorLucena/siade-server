function loadPage(link){
	$(".content").load(link);
	return false;
}

function sendForm(form){
	alert ("may work (someday)");
	/*var dados = form.serialize();
	var url = form.action;
	$.ajax({
		type: "post",
		url: url,
		data: dados,
		success: function(page){
			$(".content").html(page);
		}
	});*/
	return false;
}