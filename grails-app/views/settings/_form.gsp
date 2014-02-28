<%@ page import="com.br.holocronifrn.siadeserver.Settings" %>



<div class="fieldcontain ${hasErrors(bean: settingsInstance, field: 'city', 'error')} required">
	<label for="city">
		<g:message code="settings.city.label" default="City" />
		<span class="required-indicator">*</span>
	</label>
	<g:select id="city" name="city.id" from="${com.br.holocronifrn.siadeserver.City.list()}" optionKey="id" required="" value="${settingsInstance?.city?.id}" class="many-to-one"/>
</div>

<div class="fieldcontain ${hasErrors(bean: settingsInstance, field: 'state', 'error')} required">
	<label for="state">
		<g:message code="settings.state.label" default="State" />
		<span class="required-indicator">*</span>
	</label>
	<g:select id="state" name="state.id" from="${com.br.holocronifrn.siadeserver.State.list()}" optionKey="id" required="" value="${settingsInstance?.state?.id}" class="many-to-one"/>
</div>

