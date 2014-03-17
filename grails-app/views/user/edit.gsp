<g:set var="entityName" value="${message(code: 'user.label', default: 'User')}" />
<br />
<div id="edit-user" class="panel panel-default content scaffold-edit" role="main">
	<div class="panel-heading">
		<g:message code="default.edit.label" args="[entityName]" />
	</div>
	<g:if test="${flash.message}">
		<div class="message" role="status">${flash.message}</div>
	</g:if>
	<g:hasErrors bean="${userInstance}">
	<ul class="errors" role="alert">
		<g:eachError bean="${userInstance}" var="error">
		<li <g:if test="${error in org.springframework.validation.FieldError}">data-field-id="${error.field}"</g:if>><g:message error="${error}"/></li>
		</g:eachError>
	</ul>
	</g:hasErrors>
	<div class="panel-body">
		<g:form onsubmit="sendForm(this);return false" url="[resource:userInstance, action:'update']" method="PUT" >
				<g:hiddenField name="version" value="${userInstance?.version}" />
				<fieldset class="form">
					<g:render template="form"/>
				</fieldset>
				<fieldset class="buttons">
					<g:actionSubmit class="save btn btn-default" action="update" value="${message(code: 'default.button.update.label', default: 'Update')}" />
				</fieldset>
			</g:form>
	</div>
</div>