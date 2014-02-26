<g:set var="entityName" value="${message(code: 'district.label', default: 'District')}" />
<div class="row">
	<div class="col-lg-12">
		<h1 class="page-header">
		<g:message code="default.list.label" args="[entityName]" />
		</h1>
	</div>
</div>
<div id="list-district" class="content scaffold-list panel panel-default" role="main">
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
					
						<g:sortableColumn property="name" title="${message(code: 'district.name.label', default: 'Name')}" />
					
						<th><g:message code="district.city.label" default="City" /></th>
					
					</tr>
				</thead>
				<tbody>
				<g:each in="${districtInstanceList}" status="i" var="districtInstance">
					<tr class="${(i % 2) == 0 ? 'even' : 'odd'}">
						
						<td><a href="#" onclick="loadPage('<g:createLink action="show" id="${districtInstance.id}" />')">${fieldValue(bean: districtInstance, field: "name")}</a></td>
					
						<td>${fieldValue(bean: districtInstance, field: "city")}</td>
					
					</tr>
				</g:each>
				</tbody>
			</table>
			<div class="pagination">
				<g:paginate total="${districtInstanceCount ?: 0}" />
			</div>
	</div>
</div>
