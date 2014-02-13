
<%@ page import="com.br.holocronifrn.siadeserver.Still"%>

<g:set var="entityName"
	value="${message(code: 'still.label', default: 'Still')}" />



<div class="row">
	<div class="col-lg-12">
		<h1 class="page-header">
			<g:message code="default.list.label" args="[entityName]" />
		</h1>
	</div>
</div>


<div class="row">
	<div class="col-lg-12">
		<div class="panel panel-default">
			<div class="panel-heading">
				<g:message code="default.list.label" args="[entityName]" />
			</div>

			<div class="panel-body">
				<div id="list-still" class="content scaffold-list table-response"
					role="main">
					<g:if test="${flash.message}">
						<div class="message" role="status">
							${flash.message}
						</div>
					</g:if>
					<table
						class="table table-striped table-bordered table-hover dataTable no-footer"
						id="dataTables-example" aria-describedby="dataTables-example_info">
						<thead>
							<tr role="row">
								<g:sortableColumn property="habitants_amount"
									title="${message(code: 'still.habitants_amount.label', default: 'Habitantsamount')}" />

								<g:sortableColumn property="dogs_amount"
									title="${message(code: 'still.dogs_amount.label', default: 'Dogsamount')}" />

								<g:sortableColumn property="cats_amount"
									title="${message(code: 'still.cats_amount.label', default: 'Catsamount')}" />

								<g:sortableColumn property="still_number"
									title="${message(code: 'still.still_number.label', default: 'Stillnumber')}" />

								<g:sortableColumn property="idStillTipe"
									title="${message(code: 'still.idStillTipe.label', default: 'Id Still Tipe')}" />

								<th><g:message code="still.side.label" default="Side" />
							</tr>
						</thead>
						<tbody>
							<g:each in="${stillInstanceList}" status="i" var="stillInstance">
								<tr class="${(i % 2) == 0 ? 'even' : 'odd'}">

									<td><g:link action="show" id="${stillInstance.id}">
											${fieldValue(bean: stillInstance, field: "habitants_amount")}
										</g:link></td>

									<td>
										${fieldValue(bean: stillInstance, field: "dogs_amount")}
									</td>

									<td>
										${fieldValue(bean: stillInstance, field: "cats_amount")}
									</td>

									<td>
										${fieldValue(bean: stillInstance, field: "still_number")}
									</td>

									<td>
										${fieldValue(bean: stillInstance, field: "idStillTipe")}
									</td>

									<td>
										${fieldValue(bean: stillInstance, field: "side")}
									</td>

								</tr>
							</g:each>
						</tbody>
					</table>
					<div class="pagination">
						<g:paginate total="${stillInstanceCount ?: 0}" />
					</div>
				</div>
			</div>
		</div>
	</div>

</div>


