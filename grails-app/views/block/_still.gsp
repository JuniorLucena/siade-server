<script type="text/javascript">
$(function($){
	var form = $("#stills").html();
	$("#addRealty").show();
	$("#addRealty").click(function(){
		
		$("#stills").append(form);
	});
});

</script>
<div id="stills">
	<div class="col-lg-12"><div class="form-group col-lg-3 fieldcontain ${hasErrors(bean: stillInstance, field: 'still_number', 'error')} required">
		<label for="still_number"> <g:message code="still.still_number.label" default="Stillnumber" />
			<span	class="required-indicator">*</span>
		</label> 
		<g:textField class="form-control" name="still_number" required="" value="${stillInstance?.still_number}" />
	</div>
	<div class="form-group col-lg-3 fieldcontain ${hasErrors(bean: stillInstance, field: "numberSequence", "error")} required">
		<label for="numberSequence">
			<g:message	code="still.numberSequence.label" default="numberSequence" />
			<span class="required-indicator">*</span>
		</label>
		<g:field class="form-control" name="numberSequence" type="number" value="${stillInstance?.numberSequence}" required="" />
	</div> 
	<div class="form-group col-lg-3 fieldcontain ${hasErrors(bean: stillInstance, field: "idStillTipe", "error")} required">
		<label for="idStillTipe">
			<g:message code="still.idStillTipe.label" default="Id Still Tipe" /> <span	class="required-indicator">*</span>
		</label>
		<g:select class="form-control" name="idStillTipe" from="${com.br.holocronifrn.siadeserver.RealtyType.list()}" optionKey="id" value="" />
	</div>
	<div class="col-lg-3">
		<br />
		<button class="btn btn-default" id="addRealty" style="display:none">Adicionar Imóvel</button>
	</div>
</div>
</div>