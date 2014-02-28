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
				<g:form
					url="[resource:settingsInstance, controller:'settings', action:'save']">
					<fieldset class="form">
						<div class="form-group">
							<label>Estados</label>

							<g:select class="form-control" id="state.id" name="state.id"
								from="${com.br.holocronifrn.siadeserver.State.list()}"
								optionKey="id" required=""
								value="${settingsInstance?.state?.id}"
								onchange="selectedState()" />

							</select> <label>Cidades</label>
							<g:select class="settingsCity form-control" id="city"
								name="city.id" from="" optionKey="id" required=""
								value="${settingsInstance?.city?.id}">
							</g:select>

						</div>

						<div class="modal-footer">
							<button type="button" class="btn btn-default"
								data-dismiss="modal">Cancelar</button>

							<g:submitButton name="create" class="save btn btn-primary"
								value="${message(code: 'default.button.create.label', default: 'Create')}" />
						</div>
					</fieldset>
				</g:form>
			</div>
		</div>
	</div>
</div>
