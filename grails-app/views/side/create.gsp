<g:set var="entityName" value="${message(code: 'side.label', default: 'Side')}" />
<br />
<div id="create-side" class="panel panel-default content scaffold-create" role="main">
	<div class="panel-heading">
		<g:message code="default.create.label" args="[entityName]" />
	</div>
	<div class="panel-body">
		<g:if test="${flash.message}">
		<div class="message" role="status">${flash.message}</div>
			</g:if>
			<g:hasErrors bean="${sideInstance}">
			<ul class="errors" role="alert">
				<g:eachError bean="${sideInstance}" var="error">
				<li <g:if test="${error in org.springframework.validation.FieldError}">data-field-id="${error.field}"</g:if>><g:message error="${error}"/></li>
				</g:eachError>
			</ul>
			</g:hasErrors>
			<g:form onsubmit="sendForm(this);return false" url="[resource:sideInstance, action:'save']" name="Lado">
				<fieldset class="form">
					<g:render template="form"/>
				</fieldset>
				<fieldset class="buttons">
					<g:submitButton name="create" class="save btn btn-primary" value="${message(code: 'default.button.create.label', default: 'Create')}" />
				</fieldset>
			</g:form>
	</div>
</div>
