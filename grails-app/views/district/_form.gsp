<%@ page import="com.br.holocronifrn.siadeserver.District" %>
<div class="fieldcontain ${hasErrors(bean: districtInstance, field: 'name', 'error')} required">
	<label for="name">
		<g:message code="district.name.label" default="Name" />
		<span class="required-indicator">*</span>
	</label>
	<g:textField class="form-control" name="name" required="" value="${districtInstance?.name}"/>
</div>
<div class="form-group fieldcontain ${hasErrors(bean: districtInstance, field: 'city', 'error')} required">
	<label for="city"> <g:message code="district.city.label"
			default="City" />
	</label>
	<g:select class="form-control" id="city" name="city.id"
		from="${com.br.holocronifrn.siadeserver.Settings.list().city}" optionKey="id"
		required="" value="${districtInstance?.city?.id}" />
</div>
