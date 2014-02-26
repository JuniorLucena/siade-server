<g:set var="entityName" value="${message(code: 'district.label', default: 'District')}" />
<div class="row">
	<div class="col-lg-12">
		<h1 class="page-header">
			<g:message code="default.create.label" args="[entityName]" />
		</h1>
	</div>
</div>
<div id="create-district" class="panel panel-default content scaffold-create" role="main">
	<div class="panel-heading">
		<g:message code="default.create.label" args="[entityName]" />
	</div>
	<div class="panel-body">
			<g:if test="${flash.message}">
			<div class="message" role="status">${flash.message}</div>
			</g:if>
			<g:hasErrors bean="${districtInstance}">
			<ul class="errors" role="alert">
				<g:eachError bean="${districtInstance}" var="error">
				<li <g:if test="${error in org.springframework.validation.FieldError}">data-field-id="${error.field}"</g:if>><g:message error="${error}"/></li>
				</g:eachError>
			</ul>
			</g:hasErrors>
			<g:form onsubmit="sendForm(this);return false" url="[resource:districtInstance, action:'save']" name="Bairro">
				<fieldset class="form">
					<g:render template="form"/>
				</fieldset>
				<fieldset class="buttons">
					<g:submitButton name="create" class="save btn btn-primary" value="${message(code: 'default.button.create.label', default: 'Create')}" />
				</fieldset>
			</g:form>
	</div>
</div>
