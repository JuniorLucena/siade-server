<%@ page import="com.br.holocronifrn.siadeserver.UserLevel" %>



<div class="fieldcontain ${hasErrors(bean: userLevelInstance, field: 'authority', 'error')} required">
	<label for="authority">
		<g:message code="userLevel.authority.label" default="Authority" />
		<span class="required-indicator">*</span>
	</label>
	<g:textField name="authority" required="" value="${userLevelInstance?.authority}"/>
</div>

