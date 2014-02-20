<g:set var="entityName" value="${message(code: 'user.label', default: 'User')}" />
<div id="list-state"  class="content scaffold-list panel panel-default" role="main">
	<div class="panel-heading">
		<g:message code="default.list.label" args="[entityName]" />
	</div>
	<div class="panel-body">
		<g:if test="${flash.message}">
			<div class="message" role="status">${flash.message}</div>
		</g:if>
		<table class="table table-striped table-bordered table-hover" >
			<thead>
				<tr>
					<g:sortableColumn property="username" title="${message(code: 'user.username.label', default: 'Username')}" />	
					
					<g:sortableColumn property="accountExpired" title="${message(code: 'user.accountExpired.label', default: 'Account Expired')}" />
					
					<g:sortableColumn property="accountLocked" title="${message(code: 'user.accountLocked.label', default: 'Account Locked')}" />
					
					<g:sortableColumn property="enabled" title="${message(code: 'user.enabled.label', default: 'Enabled')}" />
					
					<g:sortableColumn property="passwordExpired" title="${message(code: 'user.passwordExpired.label', default: 'Password Expired')}" />
					
				</tr>
			</thead>
			<tbody>
				<g:each in="${userInstanceList}" status="i" var="userInstance">
					<tr class="${(i % 2) == 0 ? 'even' : 'odd'}">
					
						<td><g:link action="show" id="${userInstance.id}">${fieldValue(bean: userInstance, field: "username")}</g:link></td>
					
						<td><g:formatBoolean boolean="${userInstance.accountExpired}" /></td>
					
						<td><g:formatBoolean boolean="${userInstance.accountLocked}" /></td>
					
						<td><g:formatBoolean boolean="${userInstance.enabled}" /></td>
					
						<td><g:formatBoolean boolean="${userInstance.passwordExpired}" /></td>
					
					</tr>
				</g:each>
				</tbody>
			</table>
			<div class="pagination">
				<g:paginate total="${userInstanceCount ?: 0}" />
			</div>
	</div>
</div>