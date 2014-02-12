
<%@ page import="com.br.holocronifrn.siadeserver.Still" %>
<!DOCTYPE html>
<html>
	<head>
		<meta name="layout" content="main">
		<g:set var="entityName" value="${message(code: 'still.label', default: 'Still')}" />
		<title><g:message code="default.show.label" args="[entityName]" /></title>
	</head>
	<body>
		<a href="#show-still" class="skip" tabindex="-1"><g:message code="default.link.skip.label" default="Skip to content&hellip;"/></a>
		<div class="nav" role="navigation">
			<ul>
				<li><a class="home" href="${createLink(uri: '/')}"><g:message code="default.home.label"/></a></li>
				<li><g:link class="list" action="index"><g:message code="default.list.label" args="[entityName]" /></g:link></li>
				<li><g:link class="create" action="create"><g:message code="default.new.label" args="[entityName]" /></g:link></li>
			</ul>
		</div>
		<div id="show-still" class="content scaffold-show" role="main">
			<h1><g:message code="default.show.label" args="[entityName]" /></h1>
			<g:if test="${flash.message}">
			<div class="message" role="status">${flash.message}</div>
			</g:if>
			<ol class="property-list still">
			
				<g:if test="${stillInstance?.habitants_amount}">
				<li class="fieldcontain">
					<span id="habitants_amount-label" class="property-label"><g:message code="still.habitants_amount.label" default="Habitantsamount" /></span>
					
						<span class="property-value" aria-labelledby="habitants_amount-label"><g:fieldValue bean="${stillInstance}" field="habitants_amount"/></span>
					
				</li>
				</g:if>
			
				<g:if test="${stillInstance?.dogs_amount}">
				<li class="fieldcontain">
					<span id="dogs_amount-label" class="property-label"><g:message code="still.dogs_amount.label" default="Dogsamount" /></span>
					
						<span class="property-value" aria-labelledby="dogs_amount-label"><g:fieldValue bean="${stillInstance}" field="dogs_amount"/></span>
					
				</li>
				</g:if>
			
				<g:if test="${stillInstance?.cats_amount}">
				<li class="fieldcontain">
					<span id="cats_amount-label" class="property-label"><g:message code="still.cats_amount.label" default="Catsamount" /></span>
					
						<span class="property-value" aria-labelledby="cats_amount-label"><g:fieldValue bean="${stillInstance}" field="cats_amount"/></span>
					
				</li>
				</g:if>
			
				<g:if test="${stillInstance?.still_number}">
				<li class="fieldcontain">
					<span id="still_number-label" class="property-label"><g:message code="still.still_number.label" default="Stillnumber" /></span>
					
						<span class="property-value" aria-labelledby="still_number-label"><g:fieldValue bean="${stillInstance}" field="still_number"/></span>
					
				</li>
				</g:if>
			
				<g:if test="${stillInstance?.idStillTipe}">
				<li class="fieldcontain">
					<span id="idStillTipe-label" class="property-label"><g:message code="still.idStillTipe.label" default="Id Still Tipe" /></span>
					
						<span class="property-value" aria-labelledby="idStillTipe-label"><g:fieldValue bean="${stillInstance}" field="idStillTipe"/></span>
					
				</li>
				</g:if>
			
				<g:if test="${stillInstance?.side}">
				<li class="fieldcontain">
					<span id="side-label" class="property-label"><g:message code="still.side.label" default="Side" /></span>
					
						<span class="property-value" aria-labelledby="side-label"><g:link controller="side" action="show" id="${stillInstance?.side?.id}">${stillInstance?.side?.encodeAsHTML()}</g:link></span>
					
				</li>
				</g:if>
			
			</ol>
			<g:form url="[resource:stillInstance, action:'delete']" method="DELETE">
				<fieldset class="buttons">
					<g:link class="edit" action="edit" resource="${stillInstance}"><g:message code="default.button.edit.label" default="Edit" /></g:link>
					<g:actionSubmit class="delete" action="delete" value="${message(code: 'default.button.delete.label', default: 'Delete')}" onclick="return confirm('${message(code: 'default.button.delete.confirm.message', default: 'Are you sure?')}');" />
				</fieldset>
			</g:form>
		</div>
	</body>
</html>
