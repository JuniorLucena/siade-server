<g:set var="entityName"
	value="${message(code: 'state.label', default: 'Still')}" />
<div class="row">
	<div class="col-lg-12">
		<h1 class="page-header">
			<g:message code="default.edit.label" args="[entityName]" />
		</h1>
	</div>
</div>
<div id="edit-still" class="content scaffold-edit panel panel-default"
	role="main">
	<div class="panel-heading">
		<g:message code="default.edit.label" args="[entityName]" />
	</div>
	<div class="panel-body">
		<g:if test="${flash.message}">
			<div class="message" role="status">
				${flash.message}
			</div>
		</g:if>
		<g:hasErrors bean="${stillInstance}">
			<ul class="errors" role="alert">
				<g:eachError bean="${stillInstance}" var="error">
					<li
						<g:if test="${error in org.springframework.validation.FieldError}">data-field-id="${error.field}"</g:if>><g:message
							error="${error}" /></li>
				</g:eachError>
			</ul>
		</g:hasErrors>
		<g:form onsubmit="sendForm(this);return false"
			url="[resource:stillInstance, action:'update']" method="PUT">
			<g:hiddenField name="version" value="${stillInstance?.version}" />
			<fieldset class="form">
				<g:render template="form" />
			</fieldset>
			<fieldset class="buttons">
				<g:actionSubmit class="save btn btn-primary" action="update"
					value="${message(code: 'default.button.update.label', default: 'Update')}" />
			</fieldset>
		</g:form>
		<div class="pagination">
			<g:paginate total="${stateInstanceCount ?: 0}" />
		</div>
	</div>
</div>