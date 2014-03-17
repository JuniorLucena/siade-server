<g:set var="entityName" value="${message(code: 'street.label', default: 'Street')}" />
<br />
<div id="edit-street" class="panel panel-default content scaffold-edit" role="main">
	<div class="panel-heading">
		<g:message code="default.edit.label" args="[entityName]" />
	</div>
			<g:if test="${flash.message}">
			<div class="message" role="status">${flash.message}</div>
			</g:if>
			<g:hasErrors bean="${streetInstance}">
			<ul class="errors" role="alert">
				<g:eachError bean="${streetInstance}" var="error">
				<li <g:if test="${error in org.springframework.validation.FieldError}">data-field-id="${error.field}"</g:if>><g:message error="${error}"/></li>
				</g:eachError>
			</ul>
			</g:hasErrors>
			<div class="panel-body">
			<g:form onsubmit="sendForm(this);return false" url="[resource:streetInstance, action:'update']" name="Rua" >
				<g:hiddenField name="version" value="${streetInstance?.version}" />
				<fieldset class="form">
					<g:render template="form"/>
				</fieldset>
				<fieldset class="buttons">
					<g:actionSubmit class="save btn btn-default" action="update" value="${message(code: 'default.button.update.label', default: 'Update')}" />
				</fieldset>
			</g:form>
		</div>
</div>
