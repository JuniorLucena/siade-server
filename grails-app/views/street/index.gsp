<g:set var="entityName" value="${message(code: 'street.label', default: 'Street')}" />
<div class="row">
	<div class="col-lg-12">
		<h1 class="page-header">
		<g:message code="default.list.label" args="[entityName]" />
		</h1>
	</div>
</div>
<div id="list-street" class="content scaffold-list panel panel-default" role="main">
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
					
						<g:sortableColumn property="name" title="${message(code: 'street.name.label', default: 'Name')}" />
					</tr>
				</thead>
				<tbody>
				<g:each in="${streetInstanceList}" status="i" var="streetInstance">
					<tr class="${(i % 2) == 0 ? 'even' : 'odd'}">
					
						<td><a href="#" onclick="loadPage('<g:createLink action="show" id="${streetInstance.id}" />')">${fieldValue(bean: streetInstance, field: "name")}</a></td>
					
					</tr>
				</g:each>
				</tbody>
			</table>
			<div class="pagination">
				<g:paginate total="${streetInstanceCount ?: 0}" />
			</div>
		</div>
</div>