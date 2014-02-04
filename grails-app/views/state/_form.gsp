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
<br />

