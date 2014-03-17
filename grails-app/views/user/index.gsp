<g:set var="entityName" value="${message(code: 'user.label', default: 'User')}" />
<br />
<div id="list-state"  class="content scaffold-list panel panel-default" role="main">
	<div class="panel-heading">
		<g:message code="default.list.label" args="[entityName]" />
	</div>
		<div class="panel-body">
			<g:if test="${flash.message}">
				<div class="message" role="status">${flash.message}</div>
			</g:if>
			<table class="table table-striped table-bordered table-hover">
			<thead>
				<tr>
					<g:sortableColumn property="username" title="${message(code: 'user.username.label', default: 'Username')}" />	
					
					<g:sortableColumn property="authority" title="${message(code: 'user.authority.label', default: 'Authority')}" />

					<g:sortableColumn property="code" title="${message(code: 'user.code.label', default: 'Code')}" />

					<g:sortableColumn property="gender" title="${message(code: 'user.gender.label', default: 'Gender')}" />

					<g:sortableColumn property="phone" title="${message(code: 'user.phone.label', default: 'Phone')}" />
					
					<g:sortableColumn property="cell" title="${message(code: 'user.cell.label', default: 'Cell')}" />

				</tr>
			</thead>
			<tbody>
				<g:each in="${userInstanceList}" status="i" var="userInstance">
					<tr class="${(i % 2) == 0 ? 'even' : 'odd'}">
					
						<td><a href="#" onclick="loadPage('<g:createLink action="show" id="${userInstance.id}" />')">${fieldValue(bean: userInstance, field: "username")}</a></td>

						<td><a href="#" onclick="loadPage('<g:createLink action="show" id="${userInstance.id}" />')">${fieldValue(bean: userInstance, field: "authorities")}</a></td>

						<td><a href="#" onclick="loadPage('<g:createLink action="show" id="${userInstance.id}" />')">${fieldValue(bean: userInstance, field: "code")}</a></td>

						<td><a href="#" onclick="loadPage('<g:createLink action="show" id="${userInstance.id}" />')">${fieldValue(bean: userInstance, field: "gender")}</a></td>

						<td><a href="#" onclick="loadPage('<g:createLink action="show" id="${userInstance.id}" />')">${fieldValue(bean: userInstance, field: "phone")}</a></td>

						<td><a href="#" onclick="loadPage('<g:createLink action="show" id="${userInstance.id}" />')">${fieldValue(bean: userInstance, field: "cell")}</a></td>
					
					</tr>
				</g:each>
				</tbody>
			</table>
			<div class="pagination">
				<g:paginate total="${userInstanceCount ?: 0}" />
			</div>
		</div>
	
</div>