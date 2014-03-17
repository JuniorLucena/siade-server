<%@ page import="com.br.holocronifrn.siadeserver.Side" %>



<div class="fieldcontain ${hasErrors(bean: sideInstance, field: 'number', 'error')} required">
	<label for="number">
		<g:message code="side.number.label" default="Number" />
		<span class="required-indicator">*</span>
	</label>
	<g:field name="number" type="number" value="${sideInstance.number}" required=""/>
</div>

<div class="fieldcontain ${hasErrors(bean: sideInstance, field: 'block', 'error')} required">
	<label for="block">
		<g:message code="side.block.label" default="Block" />
		<span class="required-indicator">*</span>
	</label>
	<g:select id="block" name="block.id" from="${com.br.holocronifrn.siadeserver.Block.list()}" optionKey="id" required="" value="${sideInstance?.block?.id}" class="many-to-one"/>
</div>

<div class="fieldcontain ${hasErrors(bean: sideInstance, field: 'reference', 'error')} ">
	<label for="reference">
		<g:message code="side.reference.label" default="Reference" />
		
	</label>
	<g:textField class="form-control" name="reference" value="${sideInstance?.reference}"/>
</div>

<div class="fieldcontain ${hasErrors(bean: sideInstance, field: 'street', 'error')} required">
	<label for="street">
		<g:message code="side.street.label" default="Street" />
		<span class="required-indicator">*</span>
	</label>
	<g:select id="street" name="street.id" from="${com.br.holocronifrn.siadeserver.Street.list()}" optionKey="id" required="" value="${sideInstance?.street?.id}" class="many-to-one"/>
</div>

