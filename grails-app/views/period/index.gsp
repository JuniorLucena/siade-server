
<%@ page import="com.br.holocronifrn.siadeserver.Period" %>
<!DOCTYPE html>
<html>
	<head>
		<meta name="layout" content="main">
		<g:set var="entityName" value="${message(code: 'period.label', default: 'Period')}" />
		<title><g:message code="default.list.label" args="[entityName]" /></title>
	</head>
	<body>
		<a href="#list-period" class="skip" tabindex="-1"><g:message code="default.link.skip.label" default="Skip to content&hellip;"/></a>
		<div class="nav" role="navigation">
			<ul>
				<li><a class="home" href="${createLink(uri: '/')}"><g:message code="default.home.label"/></a></li>
				<li><g:link class="create" action="create"><g:message code="default.new.label" args="[entityName]" /></g:link></li>
			</ul>
		</div>
		<div id="list-period" class="content scaffold-list" role="main">
			<h1><g:message code="default.list.label" args="[entityName]" /></h1>
			<g:if test="${flash.message}">
				<div class="message" role="status">${flash.message}</div>
			</g:if>
			<table>
			<thead>
					<tr>
					
						<g:sortableColumn property="startDate" title="${message(code: 'period.startDate.label', default: 'Start Date')}" />
					
						<g:sortableColumn property="endDate" title="${message(code: 'period.endDate.label', default: 'End Date')}" />
					
						<g:sortableColumn property="number" title="${message(code: 'period.number.label', default: 'Number')}" />
					
						<g:sortableColumn property="baseYear" title="${message(code: 'period.baseYear.label', default: 'Base Year')}" />
					
					</tr>
				</thead>
				<tbody>
				<g:each in="${periodInstanceList}" status="i" var="periodInstance">
					<tr class="${(i % 2) == 0 ? 'even' : 'odd'}">
					
						<td><g:link action="show" id="${periodInstance.id}">${fieldValue(bean: periodInstance, field: "startDate")}</g:link></td>
					
						<td><g:formatDate date="${periodInstance.endDate}" /></td>
					
						<td>${fieldValue(bean: periodInstance, field: "number")}</td>
					
						<td>${fieldValue(bean: periodInstance, field: "baseYear")}</td>
					
					</tr>
				</g:each>
				</tbody>
			</table>
			<div class="pagination">
				<g:paginate total="${periodInstanceCount ?: 0}" />
			</div>
		</div>
	</body>
</html>
