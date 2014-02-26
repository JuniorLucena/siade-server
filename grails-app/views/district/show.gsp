<g:set var="entityName" value="${message(code: 'district.label', default: 'District')}" />
<div class="row">
	<div class="col-lg-12">
		<h1 class="page-header">
			<g:message code="default.show.label" args="[entityName]" />
		</h1>
	</div>
</div>
		<div id="show-district" class="panel panel-default content scaffold-show" role="main">
			<div class="panel-heading">
				<h3>
					<g:message code="default.show.label" args="[entityName]" />
				</h3>
			</div>
			<g:if test="${flash.message}">
			<div class="message" role="status">${flash.message}</div>
			</g:if>
			<ol class="property-list district">
			
				<g:if test="${districtInstance?.name}">
				<li class="fieldcontain">
					<span id="name-label" class="property-label"><g:message code="district.name.label" default="Name" /></span>
					
						<span class="property-value" aria-labelledby="name-label"><g:fieldValue bean="${districtInstance}" field="name"/></span>
					
				</li>
				</g:if>
			
				<g:if test="${districtInstance?.blocks}">
				<li class="fieldcontain">
					<span id="blocks-label" class="property-label"><g:message code="district.blocks.label" default="Blocks" /></span>
					
						<g:each in="${districtInstance.blocks}" var="b">
						<span class="property-value" aria-labelledby="blocks-label"><g:link controller="block" action="show" id="${b.id}">${b?.encodeAsHTML()}</g:link></span>
						</g:each>
					
				</li>
				</g:if>
			
				<g:if test="${districtInstance?.city}">
				<li class="fieldcontain">
					<span id="city-label" class="property-label"><g:message code="district.city.label" default="City" /></span>
					
						<span class="property-value" aria-labelledby="city-label"><g:link controller="city" action="show" id="${districtInstance?.city?.id}">${districtInstance?.city?.encodeAsHTML()}</g:link></span>
					
				</li>
				</g:if>
			
			</ol>
		</div>
			<g:form onsubmit="sendForm(this);return false" url="[resource:districtInstance, action:'delete']" method="DELETE">
				<fieldset class="buttons">
					<a class="edit btn btn-default" onclick="loadPage('<g:createLink action="edit" resource="${districtInstance}" id="${districtInstance.id}" />')"><g:message code="default.button.edit.label" default="Edit" /></a>
					<g:actionSubmit class="delete btn btn-danger" action="delete" value="${message(code: 'default.button.delete.label', default: 'Delete')}" onclick="return confirm('${message(code: 'default.button.delete.confirm.message', default: 'Are you sure?')}');" />
				</fieldset>
			</g:form>
		

