<%@ page import="com.br.holocronifrn.siadeserver.District" %>
<<<<<<< HEAD
=======
<%@ page import="com.br.holocronifrn.siadeserver.Settings" %>



>>>>>>> 88b428531980734a0672d86dbf9e9cd130fe2e91
<div class="fieldcontain ${hasErrors(bean: districtInstance, field: 'name', 'error')} required">
	<label for="name">
		<g:message code="district.name.label" default="Name" />
		<span class="required-indicator">*</span>
	</label>
	<g:textField class="form-control" name="name" required="" value="${districtInstance?.name}"/>
</div>
<div class="form-group fieldcontain ${hasErrors(bean: districtInstance, field: 'city', 'error')} required">

	<input type="hidden" class="form-control" id="city" name="city.id" value="${Settings.get(1)?.city.id}" />
</div>
