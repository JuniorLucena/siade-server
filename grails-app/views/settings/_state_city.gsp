

<!-- modal -->
<div class="modal fade" id="myModal" tabindex="-1" role="dialog"
	aria-labelledby="myModalLabel" aria-hidden="true">
	<div class="modal-dialog">
		<div class="modal-content">
			<div class="modal-header">
				<button type="button" class="close" data-dismiss="modal"
					aria-hidden="true">&times;</button>
				<h4 class="modal-title" id="myModalLabel">Localização</h4>
			</div>
			<div class="modal-body">
				<form id="settingsStateCity" action="#">
					<div class="form-group">
						<label>Estados</label> <select id="states" class="form-control"
							name="selectState" onchange="estadoSelecionado()">
							<option>---</option>
						</select> <label>Cidades</label> <select id="settingsCity"
							class="form-control">
							<option>---</option>
						</select>

					</div>
				</form>

			</div>
			<div class="modal-footer">
				<button type="button" class="btn btn-default" data-dismiss="modal">Cancelar</button>
				<button type="button" class="btn btn-primary">Salvar</button>
			</div>
		</div>
	</div>
</div>

<script>
	$.getJSON("<g:createLinkTo dir="json" file="Estados.json" />", function(
			data) {

		$.each(data, function(key, val) {
			$("#states").append(
					"<option value=" + val.ID + ">" + val.Nome + " - "
							+ val.Sigla + "</option")
		});
	});

	function estadoSelecionado() {
		var myselect = document.getElementById("states")
		var idStateSelect = myselect.options[myselect.selectedIndex].value

		$('#settingsCity').html('<option>---</option>')
		$.getJSON("<g:createLinkTo dir="json" file="Cidades.json" />",
				function(data) {
					$.each(data, function(key, val) {
						if (val.Estado == idStateSelect) {
							$('#settingsCity').append(
									'<option value="' + val.ID + '">'
											+ val.Nome + '</option>');
							console.log(val)

						}
					});
				});
	};
</script>