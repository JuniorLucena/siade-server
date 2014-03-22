
<%@ page import="com.br.holocronifrn.siadeserver.Side" %>
<%@ page import="com.br.holocronifrn.siadeserver.RealtyType" %>
<g:set var="entityName" value="${message(code: 'block.label', default: 'Block')}" />

<div id="create-block" class="content scaffold-create" role="main">
	<g:if test="${flash.message}">
	<div class="message" role="status">${flash.message}</div>
	</g:if>
	<g:hasErrors bean="${blockInstance}">
	<ul class="errors" role="alert">
		<g:eachError bean="${blockInstance}" var="error">
		<li <g:if test="${error in org.springframework.validation.FieldError}">data-field-id="${error.field}"</g:if>><g:message error="${error}"/></li>
		</g:eachError>
	</ul>
	</g:hasErrors>
	<div class="panel panel-default">
		<div class="panel-heading">Criar Quadra</div>
		<div class="panel-body">
			<ul class="nav nav-tabs">
				<li class="active"><a href="#block" data-toogle="tab">Dados Básicos</a></li>
				<li><a href="#side" data-toogle="tab">Lados</a></li>
				<li><a href="#still" data-toogle="tab">Imóveis</a></li>
			</ul>
			<div class="tab-content">
				<div class="tab-pane fade active in" id="block" data-toogle="tab"><g:render template="block" /></div>
				<div class="tab-pane fade" id="side"  data-toogle="tab"><g:render template="side" /></div>
				<div class="tab-pane fade" id="still"  data-toogle="tab"><g:render template="still" /></div>
			</div>
			
		</div>
		<button class="btn btn-success save">Salvar</button>
	</div>
</div>
<script type="text/javascript">
	$('.panel-body a').click(function (e) {
  		e.preventDefault()
  		$(this).tab('show')
	})
</script>


