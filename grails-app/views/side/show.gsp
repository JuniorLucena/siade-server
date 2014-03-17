
<%@ page import="com.br.holocronifrn.siadeserver.Side" %>
<!DOCTYPE html>
<html>
	<head>
		<meta name="layout" content="main">
		<g:set var="entityName" value="${message(code: 'side.label', default: 'Side')}" />
		<title><g:message code="default.show.label" args="[entityName]" /></title>
	</head>
	<body>
		<a href="#show-side" class="skip" tabindex="-1"><g:message code="default.link.skip.label" default="Skip to content&hellip;"/></a>
		<div class="nav" role="navigation">
			<ul>
				<li><a class="home" href="${createLink(uri: '/')}"><g:message code="default.home.label"/></a></li>
				<li><g:link class="list" action="index"><g:message code="default.list.label" args="[entityName]" /></g:link></li>
				<li><g:link class="create" action="create"><g:message code="default.new.label" args="[entityName]" /></g:link></li>
			</ul>
		</div>
		<div id="show-side" class="content scaffold-show" role="main">
			<h1><g:message code="default.show.label" args="[entityName]" /></h1>
			<g:if test="${flash.message}">
			<div class="message" role="status">${flash.message}</div>
			</g:if>
			<ol class="property-list side">
			
				<g:if test="${sideInstance?.number}">
				<li class="fieldcontain">
					<span id="number-label" class="property-label"><g:message code="side.number.label" default="Number" /></span>
					
						<span class="property-value" aria-labelledby="number-label"><g:fieldValue bean="${sideInstance}" field="number"/></span>
					
				</li>
				</g:if>
			
				<g:if test="${sideInstance?.block}">
				<li class="fieldcontain">
					<span id="block-label" class="property-label"><g:message code="side.block.label" default="Block" /></span>
					
						<span class="property-value" aria-labelledby="block-label"><g:link controller="block" action="show" id="${sideInstance?.block?.id}">${sideInstance?.block?.encodeAsHTML()}</g:link></span>
					
				</li>
				</g:if>
			
				<g:if test="${sideInstance?.reference}">
				<li class="fieldcontain">
					<span id="reference-label" class="property-label"><g:message code="side.reference.label" default="Reference" /></span>
					
						<span class="property-value" aria-labelledby="reference-label"><g:fieldValue bean="${sideInstance}" field="reference"/></span>
					
				</li>
				</g:if>
			
				<g:if test="${sideInstance?.street}">
				<li class="fieldcontain">
					<span id="street-label" class="property-label"><g:message code="side.street.label" default="Street" /></span>
					
						<span class="property-value" aria-labelledby="street-label"><g:link controller="street" action="show" id="${sideInstance?.street?.id}">${sideInstance?.street?.encodeAsHTML()}</g:link></span>
					
				</li>
				</g:if>
			
			</ol>
			<g:form url="[resource:sideInstance, action:'delete']" method="DELETE">
				<fieldset class="buttons">
					<g:link class="edit" action="edit" resource="${sideInstance}"><g:message code="default.button.edit.label" default="Edit" /></g:link>
					<g:actionSubmit class="delete" action="delete" value="${message(code: 'default.button.delete.label', default: 'Delete')}" onclick="return confirm('${message(code: 'default.button.delete.confirm.message', default: 'Are you sure?')}');" />
				</fieldset>
			</g:form>
		</div>
	</body>
</html>
