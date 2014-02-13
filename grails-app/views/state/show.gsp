


<g:set var="entityName" value="${message(code: 'state.label', default: 'State')}" />

<div id="show-state" class="panel panel-default content scaffold-show" role="main">
<div class="panel-heading"><h3><g:message code="default.show.label" args="[entityName]" /></h3></div>
<g:if test="${flash.message}">
<div class="message" role="status">${flash.message}</div>
</g:if>
<div class="panel-body">
	<ol class="property-list state">
	
		<g:if test="${stateInstance?.name}">
		<li class="fieldcontain">
			<span id="name-label" class="property-label"><g:message code="state.name.label" default="Name" />:</span>
			
				<span class="property-value" aria-labelledby="name-label"><g:fieldValue bean="${stateInstance}" field="name"/></span>
			
		</li>
		</g:if>
	
		<g:if test="${stateInstance?.acronym}">
		<li class="fieldcontain">
			<span id="acronym-label" class="property-label"><g:message code="state.acronym.label" default="Acronym" />:</span>
			
				<span class="property-value" aria-labelledby="acronym-label"><g:fieldValue bean="${stateInstance}" field="acronym"/></span>
			
		</li>
		</g:if>
	
		<g:if test="${stateInstance?.cities}">
		<li class="fieldcontain">
			<span id="cities-label" class="property-label"><g:message code="state.cities.label" default="Cities" /></span>
			
				<g:each in="${stateInstance.cities}" var="c">
				<span class="property-value" aria-labelledby="cities-label"><g:link controller="city" action="show" id="${c.id}">${c?.encodeAsHTML()}</g:link></span>
				</g:each>
			
		</li>
		</g:if>
	
	</ol>
</div>
<g:form url="[resource:stateInstance, action:'delete']" method="DELETE">
	<fieldset class="buttons">
		<a class="edit btn btn-default" onclick="loadPage('<g:createLink action="edit" resource="${stateInstance}" id="${stateInstance.id}" />')"><g:message code="default.button.edit.label" default="Edit" /></a>
		<g:actionSubmit class="delete btn btn-danger" action="delete" value="${message(code: 'default.button.delete.label', default: 'Delete')}" onclick="return confirm('${message(code: 'default.button.delete.confirm.message', default: 'Are you sure?')}');" />
	</fieldset>
</g:form>

