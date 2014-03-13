
<%@ page import="com.br.holocronifrn.siadeserver.Side" %>
<!DOCTYPE html>
<html>
	<head>
		<meta name="layout" content="main">
		<g:set var="entityName" value="${message(code: 'side.label', default: 'Side')}" />
		<title><g:message code="default.list.label" args="[entityName]" /></title>
	</head>
	<body>
		<a href="#list-side" class="skip" tabindex="-1"><g:message code="default.link.skip.label" default="Skip to content&hellip;"/></a>
		<div class="nav" role="navigation">
			<ul>
				<li><a class="home" href="${createLink(uri: '/')}"><g:message code="default.home.label"/></a></li>
				<li><g:link class="create" action="create"><g:message code="default.new.label" args="[entityName]" /></g:link></li>
			</ul>
		</div>
		<div id="list-side" class="content scaffold-list" role="main">
			<h1><g:message code="default.list.label" args="[entityName]" /></h1>
			<g:if test="${flash.message}">
				<div class="message" role="status">${flash.message}</div>
			</g:if>
			<table>
			<thead>
					<tr>
					
						<g:sortableColumn property="number" title="${message(code: 'side.number.label', default: 'Number')}" />
					
						<th><g:message code="side.block.label" default="Block" /></th>
					
						<g:sortableColumn property="reference" title="${message(code: 'side.reference.label', default: 'Reference')}" />
					
						<th><g:message code="side.street.label" default="Street" /></th>
					
					</tr>
				</thead>
				<tbody>
				<g:each in="${sideInstanceList}" status="i" var="sideInstance">
					<tr class="${(i % 2) == 0 ? 'even' : 'odd'}">
					
						<td><g:link action="show" id="${sideInstance.id}">${fieldValue(bean: sideInstance, field: "number")}</g:link></td>
					
						<td>${fieldValue(bean: sideInstance, field: "block")}</td>
					
						<td>${fieldValue(bean: sideInstance, field: "reference")}</td>
					
						<td>${fieldValue(bean: sideInstance, field: "street")}</td>
					
					</tr>
				</g:each>
				</tbody>
			</table>
			<div class="pagination">
				<g:paginate total="${sideInstanceCount ?: 0}" />
			</div>
		</div>
	</body>
</html>
