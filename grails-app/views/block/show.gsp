
<%@ page import="com.br.holocronifrn.siadeserver.Block" %>
<!DOCTYPE html>
<html>
	<head>
		<meta name="layout" content="main">
		<g:set var="entityName" value="${message(code: 'block.label', default: 'Block')}" />
		<title><g:message code="default.show.label" args="[entityName]" /></title>
	</head>
	<body>
		<a href="#show-block" class="skip" tabindex="-1"><g:message code="default.link.skip.label" default="Skip to content&hellip;"/></a>
		<div class="nav" role="navigation">
			<ul>
				<li><a class="home" href="${createLink(uri: '/')}"><g:message code="default.home.label"/></a></li>
				<li><g:link class="list" action="index"><g:message code="default.list.label" args="[entityName]" /></g:link></li>
				<li><g:link class="create" action="create"><g:message code="default.new.label" args="[entityName]" /></g:link></li>
			</ul>
		</div>
		<div id="show-block" class="content scaffold-show" role="main">
			<h1><g:message code="default.show.label" args="[entityName]" /></h1>
			<g:if test="${flash.message}">
			<div class="message" role="status">${flash.message}</div>
			</g:if>
			<ol class="property-list block">
			
				<g:if test="${blockInstance?.identification}">
				<li class="fieldcontain">
					<span id="identification-label" class="property-label"><g:message code="block.identification.label" default="Identification" /></span>
					
						<span class="property-value" aria-labelledby="identification-label"><g:fieldValue bean="${blockInstance}" field="identification"/></span>
					
				</li>
				</g:if>
			
				<g:if test="${blockInstance?.district}">
				<li class="fieldcontain">
					<span id="district-label" class="property-label"><g:message code="block.district.label" default="District" /></span>
					
						<span class="property-value" aria-labelledby="district-label"><g:link controller="district" action="show" id="${blockInstance?.district?.id}">${blockInstance?.district?.encodeAsHTML()}</g:link></span>
					
				</li>
				</g:if>
			
				<g:if test="${blockInstance?.side}">
				<li class="fieldcontain">
					<span id="side-label" class="property-label"><g:message code="block.side.label" default="Side" /></span>
					
						<g:each in="${blockInstance.side}" var="s">
						<span class="property-value" aria-labelledby="side-label"><g:link controller="side" action="show" id="${s.id}">${s?.encodeAsHTML()}</g:link></span>
						</g:each>
					
				</li>
				</g:if>
			
			</ol>
			<g:form url="[resource:blockInstance, action:'delete']" method="DELETE">
				<fieldset class="buttons">
					<g:link class="edit" action="edit" resource="${blockInstance}"><g:message code="default.button.edit.label" default="Edit" /></g:link>
					<g:actionSubmit class="delete" action="delete" value="${message(code: 'default.button.delete.label', default: 'Delete')}" onclick="return confirm('${message(code: 'default.button.delete.confirm.message', default: 'Are you sure?')}');" />
				</fieldset>
			</g:form>
		</div>
	</body>
</html>
