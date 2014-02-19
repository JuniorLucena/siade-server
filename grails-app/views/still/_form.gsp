<%@ page import="com.br.holocronifrn.siadeserver.Still"%>

<div
	class="fieldcontain ${hasErrors(bean: stillInstance, field: 'habitants_amount', 'error')} required">
	<label for="habitants_amount"> <g:message
			code="still.habitants_amount.label" default="Habitantsamount" /> <span
		class="required-indicator">*</span>
	</label>
	<g:field class="form-control" name="habitants_amount" type="number"
		value="${stillInstance.habitants_amount}" required="" />
</div>


<div
	class="fieldcontain ${hasErrors(bean: stillInstance, field: 'dogs_amount', 'error')} required">
	<label for="dogs_amount"> <g:message
			code="still.dogs_amount.label" default="Dogsamount" /> <span
		class="required-indicator">*</span>
	</label>
	<g:field class="form-control" name="dogs_amount" type="number"
		value="${stillInstance.dogs_amount}" required="" />
</div>

<div
	class="fieldcontain ${hasErrors(bean: stillInstance, field: 'cats_amount', 'error')} required">
	<label for="cats_amount"> <g:message
			code="still.cats_amount.label" default="Catsamount" /> <span
		class="required-indicator">*</span>
	</label>
	<g:field class="form-control" name="cats_amount" type="number"
		value="${stillInstance.cats_amount}" required="" />
</div>

<div
	class="fieldcontain ${hasErrors(bean: stillInstance, field: 'still_number', 'error')} required">
	<label for="still_number"> <g:message
			code="still.still_number.label" default="Stillnumber" /> <span
		class="required-indicator">*</span>
	</label>
	<g:textField class="form-control" name="still_number" required=""
		value="${stillInstance?.still_number}" />
</div>

<div
	class="fieldcontain ${hasErrors(bean: stillInstance, field: 'idStillTipe', 'error')} required">
	<label for="idStillTipe"> <g:message
			code="still.idStillTipe.label" default="Id Still Tipe" /> <span
		class="required-indicator">*</span>
	</label>
	<g:field class="form-control" name="idStillTipe" type="number"
		value="${stillInstance.idStillTipe}" required="" />
</div>


<div
	class="fieldcontain ${hasErrors(bean: stillInstance, field: 'numberSequence', 'error')} required">
	<label for="numberSequence"> <g:message
			code="still.numberSequence.label" default="numberSequence" /> <span
		class="required-indicator">*</span>
	</label>
	<g:field class="form-control" name="numberSequence" type="number"
		value="${stillInstance.numberSequence}" required="" />
</div>

<div
	class="fieldcontain ${hasErrors(bean: stillInstance, field: 'side', 'error')} required">
	<label for="side"> <g:message code="still.side.label"
			default="Side" /> <span class="required-indicator">*</span>
	</label>
	<g:select class="form-control" id="side" name="side.id"
		from="${com.br.holocronifrn.siadeserver.Side.list()}" optionKey="id"
		required="" value="${stillInstance?.side?.id}" />
</div>

