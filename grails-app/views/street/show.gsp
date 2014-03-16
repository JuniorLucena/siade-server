<g:set var="entityName" value="${message(code: 'street.label', default: 'Street')}" />
<br />
<div id="show-street" class="panel panel-default content scaffold-show" role="main">
	<div class="panel-heading">
			<g:message code="default.show.label" args="[entityName]" />
	</div>
			<g:if test="${flash.message}">
			<div class="message" role="status">${flash.message}</div>
			</g:if>
		<div class="panel-body">
			<ol class="property-list street">
			
				<g:if test="${streetInstance?.name}">
				<li class="fieldcontain">
					<span id="name-label" class="property-label"><g:message code="street.name.label" default="Name" /></span>
					
						<span class="property-value" aria-labelledby="name-label"><g:fieldValue bean="${streetInstance}" field="name"/></span>
					
				</li>
				</g:if>
			
				<g:if test="${streetInstance?.sides}">
				<li class="fieldcontain">
					<span id="sides-label" class="property-label"><g:message code="street.sides.label" default="Sides" /></span>
					
						<g:each in="${streetInstance.sides}" var="s">
						<span class="property-value" aria-labelledby="sides-label"><g:link controller="side" action="show" id="${s.id}">${s?.encodeAsHTML()}</g:link></span>
						</g:each>
					
				</li>
				</g:if>
			
			</ol>
		</div>
</div>
			<g:form onsubmit="sendForm(this);return false" url="[resource:streetInstance, action:'delete']" method="DELETE">
				<fieldset class="buttons">
					<a class="edit btn btn-default" onclick="loadPage('<g:createLink action="edit" resource="${streetInstance}" id="${streetInstance.id}" />')">
					<g:message code="default.button.edit.label" default="Edit" /></a>
					<g:actionSubmit class="delete btn btn-danger" action="delete" value="${message(code: 'default.button.delete.label', default: 'Delete')}" onclick="return confirm('${message(code: 'default.button.delete.confirm.message', default: 'Are you sure?')}');" />
				</fieldset>
			</g:form>
