
<%@ page import="com.br.holocronifrn.siadeserver.Still" %>
<!DOCTYPE html>
<html>
	<head>
		<meta name="layout" content="main">
		<g:set var="entityName" value="${message(code: 'still.label', default: 'Still')}" />
		<title><g:message code="default.list.label" args="[entityName]" /></title>
	</head>
	<body>
		<a href="#list-still" class="skip" tabindex="-1"><g:message code="default.link.skip.label" default="Skip to content&hellip;"/></a>
		<div class="nav" role="navigation">
			<ul>
				<li><a class="home" href="${createLink(uri: '/')}"><g:message code="default.home.label"/></a></li>
				<li><g:link class="create" action="create"><g:message code="default.new.label" args="[entityName]" /></g:link></li>
			</ul>
		</div>
		<div id="list-still" class="content scaffold-list" role="main">
			<h1><g:message code="default.list.label" args="[entityName]" /></h1>
			<g:if test="${flash.message}">
				<div class="message" role="status">${flash.message}</div>
			</g:if>
			<table>
			<thead>
					<tr>
					
						<g:sortableColumn property="habitants_amount" title="${message(code: 'still.habitants_amount.label', default: 'Habitantsamount')}" />
					
						<g:sortableColumn property="dogs_amount" title="${message(code: 'still.dogs_amount.label', default: 'Dogsamount')}" />
					
						<g:sortableColumn property="cats_amount" title="${message(code: 'still.cats_amount.label', default: 'Catsamount')}" />
					
						<g:sortableColumn property="still_number" title="${message(code: 'still.still_number.label', default: 'Stillnumber')}" />
					
						<g:sortableColumn property="idStillTipe" title="${message(code: 'still.idStillTipe.label', default: 'Id Still Tipe')}" />
					
						<th><g:message code="still.side.label" default="Side" /></th>
					
					</tr>
				</thead>
				<tbody>
				<g:each in="${stillInstanceList}" status="i" var="stillInstance">
					<tr class="${(i % 2) == 0 ? 'even' : 'odd'}">
					
						<td><g:link action="show" id="${stillInstance.id}">${fieldValue(bean: stillInstance, field: "habitants_amount")}</g:link></td>
					
						<td>${fieldValue(bean: stillInstance, field: "dogs_amount")}</td>
					
						<td>${fieldValue(bean: stillInstance, field: "cats_amount")}</td>
					
						<td>${fieldValue(bean: stillInstance, field: "still_number")}</td>
					
						<td>${fieldValue(bean: stillInstance, field: "idStillTipe")}</td>
					
						<td>${fieldValue(bean: stillInstance, field: "side")}</td>
					
					</tr>
				</g:each>
				</tbody>
			</table>
			<div class="pagination">
				<g:paginate total="${stillInstanceCount ?: 0}" />
			</div>
		</div>
	</body>
</html>
