<%@ page import="com.br.holocronifrn.siadeserver.Block" %>



<div class="fieldcontain ${hasErrors(bean: blockInstance, field: 'identification', 'error')} required">
	<label for="identification">
		<g:message code="block.identification.label" default="Identification" />
		<span class="required-indicator">*</span>
	</label>
	<g:textField class="form-control" name="identification" pattern="${blockInstance.constraints.identification.matches}" required="" value="${blockInstance?.identification}"/>
</div>

<div class="fieldcontain ${hasErrors(bean: blockInstance, field: 'district', 'error')} required">
	<label for="district">
		<g:message code="block.district.label" default="District" />
		<span class="required-indicator">*</span>
	</label>
	<g:select  id="district" name="district.id" from="${com.br.holocronifrn.siadeserver.District.list()}" optionKey="id" required="" value="${blockInstance?.district?.id}" class="many-to-one form-control"/>
</div>

<div class="fieldcontain ${hasErrors(bean: blockInstance, field: 'side', 'error')} ">
	<label for="side">
		<g:message code="block.side.label" default="Side" />	
	</label>
	<input type="number" class="form-control" id="number_sides" value="1" min="1" />
	
</ul>

</div>

<script type="text/javascript">
	$(function($){
		$("#number_sides").blur(function(){
			$("#sides").html("")
			for(var i= 1; i <=$("#number_sides").val(); i++){
				$("#sides").append("Lado <p><input type='text' value='"+i+"' /> Referência<input type='text' value='referência' /></p><hr />")
			}
		});
	});
</script>