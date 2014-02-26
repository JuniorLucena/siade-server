<g:set var="entityName" value="${message(code: 'district.label', default: 'District')}" />
<div class="row">
	<div class="col-lg-12">
		<h1 class="page-header">
	<g:message code="default.edit.label" args="[entityName]" />
		</h1>
	</div>
</div>
<div id="edit-district" class="panel panel-default content scaffold-edit" role="main">
	<div class="panel-heading">
		<g:message code="default.edit.label" args="[entityName]" />
	</div>
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
			<div class="panel-body">
			<g:form onsubmit="sendForm(this);return false" url="[resource:districtInstance, action:'update']" name="Bairro" >
				<g:hiddenField name="version" value="${districtInstance?.version}" />
				<fieldset class="form">
					<g:render template="form"/>
				</fieldset>
				<fieldset class="buttons">
					<g:actionSubmit class="save btn btn-default" action="update" value="${message(code: 'default.button.update.label', default: 'Update')}" />
				</fieldset>
			</g:form>
		</div>
</div>
