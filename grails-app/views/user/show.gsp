
<g:set var="entityName" value="${message(code: 'user.label', default: 'User')}" />
<br />
<div id="show-user" class="panel panel-default content scaffold-show" role="main">

	<div class="panel-heading">
		<g:message code="default.show.label" args="[entityName]" />
	</div>
	<g:if test="${flash.message}">
	<div class="message" role="status">${flash.message}</div>
	</g:if>
		<div class="panel-body">
			<ol class="property-list user">
			
				<g:if test="${userInstance?.username}">
				<li class="fieldcontain">
					<span id="username-label" class="property-label"><g:message code="user.username.label" default="Username" /></span>
					
						<span class="property-value" aria-labelledby="username-label"><g:fieldValue bean="${userInstance}" field="username"/></span>
					
				</li>
				</g:if>

				<g:if test="${userInstance?.authorities}">
				<li class="fieldcontain">
					<span id="authorities-label" class="property-label"><g:message code="user.authorities.label" default="Authority" /></span>
					
						<span class="property-value" aria-labelledby="authorities-label"><g:fieldValue bean="${userInstance}" field="authorities"/></span>
					
				</li>
				</g:if>

				<g:if test="${userInstance?.name}">
				<li class="fieldcontain">
					<span id="name-label" class="property-label"><g:message code="user.name.label" default="Name" /></span>
					
						<span class="property-value" aria-labelledby="name-label"><g:fieldValue bean="${userInstance}" field="name"/></span>
					
				</li>
				</g:if>

				<g:if test="${userInstance?.code}">
				<li class="fieldcontain">
					<span id="code-label" class="property-label"><g:message code="user.code.label" default="Code" /></span>
					
						<span class="property-value" aria-labelledby="code-label"><g:fieldValue bean="${userInstance}" field="code"/></span>
					
				</li>
				</g:if>
			
				<g:if test="${userInstance?.gender}">
				<li class="fieldcontain">
					<span id="gender-label" class="property-label"><g:message code="user.gender.label" default="Gender" /></span>
					
						<span class="property-value" aria-labelledby="gender-label"><g:fieldValue bean="${userInstance}" field="gender"/></span>
					
				</li>
				</g:if>
				
				<g:if test="${userInstance?.address}">
				<li class="fieldcontain">
					<span id="address-label" class="property-label"><g:message code="user.address.label" default="Address" /></span>
					
						<span class="property-value" aria-labelledby="address-label"><g:link controller="address" action="show" id="${userInstance?.address?.id}">${userInstance?.address?.encodeAsHTML()}</g:link></span>
					
				</li>
				</g:if>

				<g:if test="${userInstance?.phone}">
				<li class="fieldcontain">
					<span id="phone-label" class="property-label"><g:message code="user.phone.label" default="Phone" /></span>
					
						<span class="property-value" aria-labelledby="phone-label"><g:fieldValue bean="${userInstance}" field="phone"/></span>
					
				</li>
				</g:if>

				<g:if test="${userInstance?.cell}">
				<li class="fieldcontain">
					<span id="cell-label" class="property-label"><g:message code="user.cell.label" default="Cell" /></span>
					
						<span class="property-value" aria-labelledby="cell-label"><g:fieldValue bean="${userInstance}" field="cell"/></span>
					
				</li>
				</g:if>
			
			</ol>
			</div>
</div>
			<g:form onsubmit="sendForm(this);return false" url="[resource:userInstance, action:'delete']" method="DELETE">
				<fieldset class="buttons">
					<a class="edit btn btn-default" onclick="loadPage('<g:createLink action="edit" resource="${userInstance}" id="${userInstance.id}" />')">
					<g:message code="default.button.edit.label" default="Edit" /></a>
					<g:actionSubmit class="delete btn btn-danger" action="delete" value="${message(code: 'default.button.delete.label', default: 'Delete')}" onclick="return confirm('${message(code: 'default.button.delete.confirm.message', default: 'Are you sure?')}');" />

				</fieldset>
				<br />
			</g:form>