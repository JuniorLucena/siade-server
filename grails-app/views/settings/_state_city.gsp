

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
						<label>Estados</label>

						<g:select class="form-control" id="state.id"
							from="${com.br.holocronifrn.siadeserver.State.list()}"
							optionKey="id" required="" value="${stateInstance?.state?.id}" onchange="selectedState()"
							name="state.id" />

						</select> <label>Cidades</label> <select id="settingsCity"
							class="form-control">
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
