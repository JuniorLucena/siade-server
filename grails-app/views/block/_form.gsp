<%@ page import="com.br.holocronifrn.siadeserver.Block" %>



<div class="fieldcontain ${hasErrors(bean: blockInstance, field: 'identification', 'error')} required">
	<label for="identification">
		<g:message code="block.identification.label" default="Identification" />
		<span class="required-indicator">*</span>
	</label>
	<g:textField name="identification" pattern="${blockInstance.constraints.identification.matches}" required="" value="${blockInstance?.identification}"/>
</div>

<div class="fieldcontain ${hasErrors(bean: blockInstance, field: 'district', 'error')} required">
	<label for="district">
		<g:message code="block.district.label" default="District" />
		<span class="required-indicator">*</span>
	</label>
	<g:select id="district" name="district.id" from="${com.br.holocronifrn.siadeserver.District.list()}" optionKey="id" required="" value="${blockInstance?.district?.id}" class="many-to-one"/>
</div>

<div class="fieldcontain ${hasErrors(bean: blockInstance, field: 'side', 'error')} ">
	<label for="side">
		<g:message code="block.side.label" default="Side" />
		
	</label>
	
<ul class="one-to-many">
<g:each in="${blockInstance?.side?}" var="s">
    <li><g:link controller="side" action="show" id="${s.id}">${s?.encodeAsHTML()}</g:link></li>
</g:each>
<li class="add">
<g:link controller="side" action="create" params="['block.id': blockInstance?.id]">${message(code: 'default.add.label', args: [message(code: 'side.label', default: 'Side')])}</g:link>
</li>
</ul>

</div>

