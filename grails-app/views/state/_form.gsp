<%@ page import="com.br.holocronifrn.siadeserver.State" %>



<div class="fieldcontain ${hasErrors(bean: stateInstance, field: 'name', 'error')} required">
	<label for="name">
		<g:message code="state.name.label" default="Name" />
		<span class="required-indicator">*</span>
	</label>
	<g:textField class="form-control" name="name" required="" value="${stateInstance?.name}"/>
</div>

<div class="fieldcontain ${hasErrors(bean: stateInstance, field: 'acronym', 'error')} required">
	<label for="acronym">
		<g:message code="state.acronym.label" default="Acronym" />
		<span class="required-indicator">*</span>
	</label>
	<g:textField class="form-control" name="acronym" pattern="${stateInstance.constraints.acronym.matches}" required="" value="${stateInstance?.acronym}"/>
</div>

<div class="fieldcontain ${hasErrors(bean: stateInstance, field: 'cities', 'error')} ">
	<label for="cities">
		<g:message code="state.cities.label" default="Cities" />
		
	</label>
	
<ul style="list-style-type:none" class="one-to-many">
<g:each in="${stateInstance?.cities?}" var="c">
   <li><g:link controller="city" action="show" id="${c.id}">${c?.encodeAsHTML()}</g:link></li>
</g:each>
<li class="add">
<g:link class="btn btn-default" controller="city" action="create" params="['state.id': stateInstance?.id]">${message(code: 'default.add.label', args: [message(code: 'city.label', default: 'City')])}</g:link>
<g:link class="list btn btn-default" action="index"><g:message code="default.list.label" args="[entityName]" /></g:link></li>
</li>
</ul>

</div>

