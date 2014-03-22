<div id="sides">
	<hr />
	<div class="fieldcontain ${hasErrors(bean: sideInstance, field: 'number', 'error')} required">
		<label for="number">
			<g:message code="side?.number?.label" default="Number" />
			<span class="required-indicator">*</span>
		</label>
		<g:field class="form-control" name="number" type="number" value="${sideInstance?.number}" required=""/>
	</div>
</div> 