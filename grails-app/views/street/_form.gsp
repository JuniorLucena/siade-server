<%@ page import="com.br.holocronifrn.siadeserver.Street" %>



<div class="fieldcontain ${hasErrors(bean: streetInstance, field: 'name', 'error')} required">
	<label for="name">
		<g:message code="street.name.label" default="Name" />
		<span class="required-indicator">*</span>
	</label>
	<g:textField class="form-control" name="name" required="" value="${streetInstance?.name}"/>
</div>

<div class="form-group fieldcontain ${hasErrors(bean: streetInstance, field: 'sides', 'error')} required">
	<label for="sides">
		<g:message code="street.sides.label" default="Sides" />
	</label>
	
<g:select class="form-control" id="side" name="side.id"
		from="${com.br.holocronifrn.siadeserver.Side.list()}" optionKey="id"
		required="" value="${streettInstance?.sides?.id}" />
</div>
<br />