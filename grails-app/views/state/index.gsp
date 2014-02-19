<g:set var="entityName" value="${message(code: 'state.label', default: 'State')}" />
<div class="row">
	<div class="col-lg-12">
		<h1 class="page-header">
			<g:message code="default.list.label" args="[entityName]" />
		</h1>
	</div>
</div>
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
				
					<g:sortableColumn property="name" title="${message(code: 'state.name.label', default: 'Name')}" />
				
					<g:sortableColumn property="acronym" title="${message(code: 'state.acronym.label', default: 'Acronym')}" />
				
				</tr>
			</thead>
			<tbody>
			<g:each in="${stateInstanceList}" status="i" var="stateInstance">
				<tr class="${(i % 2) == 0 ? 'even' : 'odd'}">
				
					<td><a href="#" onclick="loadPage('<g:createLink action="show" id="${stateInstance.id}" />')">${fieldValue(bean: stateInstance, field: "name")}</a></td>
				
					<td>${fieldValue(bean: stateInstance, field: "acronym")}</td>
				
				</tr>
			</g:each>
			</tbody>
		</table>
	</div>
	<div class="pagination">
		<g:paginate total="${stateInstanceCount ?: 0}" />
	</div>
</div>

