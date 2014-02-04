<%@ page import="com.br.holocronifrn.siadeserver.State" %>
<!DOCTYPE html>
<html>
	<head>
		<meta name="layout" content="main">
		<g:set var="entityName" value="${message(code: 'state.label', default: 'State')}" />
		<title><g:message code="default.edit.label" args="[entityName]" /></title>
	</head>
	<body>
		<div id="edit-state" class="panel panel-default content scaffold-edit" role="main">
			<div class="panel-heading"><h1><g:message code="default.edit.label" args="[entityName]" /></h1></div>
			<g:if test="${flash.message}">
			<div class="message" role="status">${flash.message}</div>
			</g:if>
			<g:hasErrors bean="${stateInstance}">
			<ul class="errors" role="alert">
				<g:eachError bean="${stateInstance}" var="error">
				<li <g:if test="${error in org.springframework.validation.FieldError}">data-field-id="${error.field}"</g:if>><g:message error="${error}"/></li>
				</g:eachError>
			</ul>
			</g:hasErrors>
			<div class="panel-body">
				<g:form url="[resource:stateInstance, action:'update']" method="PUT" >
					<g:hiddenField name="version" value="${stateInstance?.version}" />
					<fieldset class="form">
						<g:render template="form"/>
					</fieldset>
					<fieldset class="buttons">
						<g:actionSubmit class="save btn btn-default" action="update" value="${message(code: 'default.button.update.label', default: 'Update')}" />
					</fieldset>
				</g:form>
			</div>
		</div>
	</body>
</html>
