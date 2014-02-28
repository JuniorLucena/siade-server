
<%@ page import="com.br.holocronifrn.siadeserver.Settings" %>
<!DOCTYPE html>
<html>
	<head>
		<meta name="layout" content="main">
		<g:set var="entityName" value="${message(code: 'settings.label', default: 'Settings')}" />
		<title><g:message code="default.show.label" args="[entityName]" /></title>
	</head>
	<body>
		<a href="#show-settings" class="skip" tabindex="-1"><g:message code="default.link.skip.label" default="Skip to content&hellip;"/></a>
		<div class="nav" role="navigation">
			<ul>
				<li><a class="home" href="${createLink(uri: '/')}"><g:message code="default.home.label"/></a></li>
				<li><g:link class="list" action="index"><g:message code="default.list.label" args="[entityName]" /></g:link></li>
				<li><g:link class="create" action="create"><g:message code="default.new.label" args="[entityName]" /></g:link></li>
			</ul>
		</div>
		<div id="show-settings" class="content scaffold-show" role="main">
			<h1><g:message code="default.show.label" args="[entityName]" /></h1>
			<g:if test="${flash.message}">
			<div class="message" role="status">${flash.message}</div>
			</g:if>
			<ol class="property-list settings">
			
				<g:if test="${settingsInstance?.city}">
				<li class="fieldcontain">
					<span id="city-label" class="property-label"><g:message code="settings.city.label" default="City" /></span>
					
						<span class="property-value" aria-labelledby="city-label"><g:link controller="city" action="show" id="${settingsInstance?.city?.id}">${settingsInstance?.city?.encodeAsHTML()}</g:link></span>
					
				</li>
				</g:if>
			
				<g:if test="${settingsInstance?.state}">
				<li class="fieldcontain">
					<span id="state-label" class="property-label"><g:message code="settings.state.label" default="State" /></span>
					
						<span class="property-value" aria-labelledby="state-label"><g:link controller="state" action="show" id="${settingsInstance?.state?.id}">${settingsInstance?.state?.encodeAsHTML()}</g:link></span>
					
				</li>
				</g:if>
			
			</ol>
			<g:form url="[resource:settingsInstance, action:'delete']" method="DELETE">
				<fieldset class="buttons">
					<g:link class="edit" action="edit" resource="${settingsInstance}"><g:message code="default.button.edit.label" default="Edit" /></g:link>
					<g:actionSubmit class="delete" action="delete" value="${message(code: 'default.button.delete.label', default: 'Delete')}" onclick="return confirm('${message(code: 'default.button.delete.confirm.message', default: 'Are you sure?')}');" />
				</fieldset>
			</g:form>
		</div>
	</body>
</html>
