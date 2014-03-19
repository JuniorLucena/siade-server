<%@ page import="com.br.holocronifrn.siadeserver.User" %>



<div class="fieldcontain ${hasErrors(bean: userInstance, field: 'username', 'error')} required">
	<label for="username">
		<g:message code="user.username.label" default="Username" />
		<span class="required-indicator">*</span>
	</label>
	<g:textField id="create_username"class="form-control" name="username" required="" value="${userInstance?.username}"/>
</div>

<div class="fieldcontain ${hasErrors(bean: userInstance, field: 'password', 'error')} required">
	<label for="password">
		<g:message code="user.password.label" default="Password" />
		<span class="required-indicator">*</span>
	</label>
	<g:textField class="form-control" name="password" required="" value="${userInstance?.password}"/>
</div>

<div class="fieldcontain ${hasErrors(bean: userInstance, field: 'address', 'error')} required">
	<label for="address">
		<g:message code="user.address.label" default="Address" />
	</label>
	<g:select id="address" name="address.id" from="${com.br.holocronifrn.siadeserver.Address.list()}" optionKey="id" value="${userInstance?.address?.id}" class="form-control"/>
</div>


<div class="fieldcontain ${hasErrors(bean: userLevelInstance, field: 'authority', 'error')} required">
	<label for="authority">
		<g:message code="userLevel.authority.label" default="Authority" />
		<span class="required-indicator">*</span>
	</label>
	<div>
		<label>
			<g:message code="userLevel.authority.admin.label" default="Supervisor" />
		</label>
		<g:radio name="authority" required="" value='ROLE_ADMIN'/>
		<label>
			<g:message code="userLevel.authority.user.label" default="Agent" />
		</label>
		<g:radio name="authority" required="" value='ROLE_USER'/>
	</div>
</div>

<div class="fieldcontain ${hasErrors(bean: userInstance, field: 'name', 'error')} required">
	<label for="name">
		<g:message code="user.name.label" default="Name" />
		<span class="required-indicator">*</span>
	</label>
	<g:textField class="form-control" name="name" required="" value="${userInstance?.name}"/>
</div>

<div class="fieldcontain ${hasErrors(bean: userInstance, field: 'code', 'error')} required">
	<label for="code">
		<g:message code="user.code.label" default="Code" />
		<span class="required-indicator">*</span>
	</label>
	<g:textField class="form-control" name="code" required="" value="${userInstance?.code}"/>
</div>




<div class="fieldcontain ${hasErrors(bean: userInstance, field: 'gender', 'error')} required">
	<label for="gender">
		<g:message code="user.gender.label" default="Gender" />
	</label>
	<div>
		<label>
			<g:message code="user.gender.male.label" default="Male" />
		</label>
		<g:radio name="gender" value="m" />
		<label>
			<g:message code="user.gender.feme.label" default="Female" />
		</label>
		<g:radio name="gender" value="f"/>
	</div>
</div>


<div class="fieldcontain ${hasErrors(bean: userInstance, field: 'phone', 'error')} required">
	<label for="phone">
		<g:message code="user.phone.label" default="Phone" />
	</label>
	<g:textField class="form-control" name="phone" value="${userInstance?.phone}"/>
</div>

<div class="fieldcontain ${hasErrors(bean: userInstance, field: 'cell', 'error')} required">
	<label for="cell">
		<g:message code="user.cell.label" default="Cell" />
	</label>
	<g:textField class="form-control" name="cell" value="${userInstance?.cell}"/>
</div>
<br />


<!--
<div class="fieldcontain ${hasErrors(bean: userInstance, field: 'accountExpired', 'error')} ">
	<label for="accountExpired">
		<g:message code="user.accountExpired.label" default="Account Expired" />
		
	</label>
	<g:checkBox name="accountExpired" value="${userInstance?.accountExpired}" />
</div>

<div class="fieldcontain ${hasErrors(bean: userInstance, field: 'accountLocked', 'error')} ">
	<label for="accountLocked">
		<g:message code="user.accountLocked.label" default="Account Locked" />
		
	</label>
	<g:checkBox name="accountLocked" value="${userInstance?.accountLocked}" />
</div>

<div class="fieldcontain ${hasErrors(bean: userInstance, field: 'enabled', 'error')} ">
	<label for="enabled">
		<g:message code="user.enabled.label" default="Enabled" />
		
	</label>
	<g:checkBox name="enabled" value="${userInstance?.enabled}" />
</div>

<div class="fieldcontain ${hasErrors(bean: userInstance, field: 'passwordExpired', 'error')} ">
	<label for="passwordExpired">
		<g:message code="user.passwordExpired.label" default="Password Expired" />
		
	</label>
	<g:checkBox name="passwordExpired" value="${userInstance?.passwordExpired}" />
</div>
-->