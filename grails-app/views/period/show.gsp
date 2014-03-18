
<%@ page import="com.br.holocronifrn.siadeserver.Period" %>
<!DOCTYPE html>
<html>
	<head>
		<meta name="layout" content="main">
		<g:set var="entityName" value="${message(code: 'period.label', default: 'Period')}" />
		<title><g:message code="default.show.label" args="[entityName]" /></title>
	</head>
	<body>
		<a href="#show-period" class="skip" tabindex="-1"><g:message code="default.link.skip.label" default="Skip to content&hellip;"/></a>
		<div class="nav" role="navigation">
			<ul>
				<li><a class="home" href="${createLink(uri: '/')}"><g:message code="default.home.label"/></a></li>
				<li><g:link class="list" action="index"><g:message code="default.list.label" args="[entityName]" /></g:link></li>
				<li><g:link class="create" action="create"><g:message code="default.new.label" args="[entityName]" /></g:link></li>
			</ul>
		</div>
		<div id="show-period" class="content scaffold-show" role="main">
			<h1><g:message code="default.show.label" args="[entityName]" /></h1>
			<g:if test="${flash.message}">
			<div class="message" role="status">${flash.message}</div>
			</g:if>
			<ol class="property-list period">
			
				<g:if test="${periodInstance?.startDate}">
				<li class="fieldcontain">
					<span id="startDate-label" class="property-label"><g:message code="period.startDate.label" default="Start Date" /></span>
					
						<span class="property-value" aria-labelledby="startDate-label"><g:formatDate date="${periodInstance?.startDate}" /></span>
					
				</li>
				</g:if>
			
				<g:if test="${periodInstance?.endDate}">
				<li class="fieldcontain">
					<span id="endDate-label" class="property-label"><g:message code="period.endDate.label" default="End Date" /></span>
					
						<span class="property-value" aria-labelledby="endDate-label"><g:formatDate date="${periodInstance?.endDate}" /></span>
					
				</li>
				</g:if>
			
				<g:if test="${periodInstance?.number}">
				<li class="fieldcontain">
					<span id="number-label" class="property-label"><g:message code="period.number.label" default="Number" /></span>
					
						<span class="property-value" aria-labelledby="number-label"><g:fieldValue bean="${periodInstance}" field="number"/></span>
					
				</li>
				</g:if>
			
				<g:if test="${periodInstance?.baseYear}">
				<li class="fieldcontain">
					<span id="baseYear-label" class="property-label"><g:message code="period.baseYear.label" default="Base Year" /></span>
					
						<span class="property-value" aria-labelledby="baseYear-label"><g:fieldValue bean="${periodInstance}" field="baseYear"/></span>
					
				</li>
				</g:if>
			
				<g:if test="${periodInstance?.users}">
				<li class="fieldcontain">
					<span id="users-label" class="property-label"><g:message code="period.users.label" default="Users" /></span>
					
						<g:each in="${periodInstance.users}" var="u">
						<span class="property-value" aria-labelledby="users-label"><g:link controller="user" action="show" id="${u.id}">${u?.encodeAsHTML()}</g:link></span>
						</g:each>
					
				</li>
				</g:if>
			
			</ol>
			<g:form url="[resource:periodInstance, action:'delete']" method="DELETE">
				<fieldset class="buttons">
					<g:link class="edit" action="edit" resource="${periodInstance}"><g:message code="default.button.edit.label" default="Edit" /></g:link>
					<g:actionSubmit class="delete" action="delete" value="${message(code: 'default.button.delete.label', default: 'Delete')}" onclick="return confirm('${message(code: 'default.button.delete.confirm.message', default: 'Are you sure?')}');" />
				</fieldset>
			</g:form>
		</div>
	</body>
</html>
