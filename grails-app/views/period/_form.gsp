<%@ page import="com.br.holocronifrn.siadeserver.Period" %>



<div class="fieldcontain ${hasErrors(bean: periodInstance, field: 'startDate', 'error')} required">
	<label for="startDate">
		<g:message code="period.startDate.label" default="Start Date" />
		<span class="required-indicator">*</span>
	</label>
	<g:datePicker name="startDate" precision="day"  value="${periodInstance?.startDate}"  />
</div>

<div class="fieldcontain ${hasErrors(bean: periodInstance, field: 'endDate', 'error')} required">
	<label for="endDate">
		<g:message code="period.endDate.label" default="End Date" />
		<span class="required-indicator">*</span>
	</label>
	<g:datePicker name="endDate" precision="day"  value="${periodInstance?.endDate}"  />
</div>

<div class="fieldcontain ${hasErrors(bean: periodInstance, field: 'number', 'error')} required">
	<label for="number">
		<g:message code="period.number.label" default="Number" />
		<span class="required-indicator">*</span>
	</label>
	<g:field name="number" type="number" value="${periodInstance.number}" required=""/>
</div>

<div class="fieldcontain ${hasErrors(bean: periodInstance, field: 'baseYear', 'error')} required">
	<label for="baseYear">
		<g:message code="period.baseYear.label" default="Base Year" />
		<span class="required-indicator">*</span>
	</label>
	<g:field name="baseYear" type="number" value="${periodInstance.baseYear}" required=""/>
</div>

<div class="fieldcontain ${hasErrors(bean: periodInstance, field: 'users', 'error')} ">
	<label for="users">
		<g:message code="period.users.label" default="Users" />
		
	</label>
	<g:select name="users" from="${com.br.holocronifrn.siadeserver.User.list()}" multiple="multiple" optionKey="id" size="5" value="${periodInstance?.users*.id}" class="many-to-many"/>
</div>

