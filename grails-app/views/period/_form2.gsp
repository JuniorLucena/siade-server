<script>
	$(document).ready(function() {
		$("#dp1").datepicker();
	});

	$(document).ready(function() {
		$("#dp2").datepicker();
	});
</script>

<div class="row">	
	<div class="col-lg-3">
		<label>Data Inicial</label>
		<div class="input-append date form-group input-group" id="dp1" data-date="" data-date-format="dd-mm-yyyy">
         	<input type="text" class="form-control">
            <span class="input-group-btn add-on">
                <button class="btn btn-default" type="button"><i class="fa fa-calendar"></i>
                </button>
            </span>
        </div>
	</div>

	<div class="col-lg-3">
		<label>Data Final</label>
		<div class="input-append date form-group input-group" id="dp2" data-date="" data-date-format="dd-mm-yyyy">
         	<input type="text" class="form-control">
            <span class="input-group-btn add-on">
                <button class="btn btn-default" type="button"><i class="fa fa-calendar"></i>
                </button>
            </span>
        </div>
	</div>
	
	<div class="col-lg-3">
		<label>Atividade</label>
		<select class="form-control">
			<option>Tratamento</option>
			<option>Pesquisa</option>
			<option>Tratamento + Pesquisa</option>
		</select>
	</div>
</div>

<button type="reset" class="btn btn-default">Reset Button</button>
<button type="submit" class="btn btn-primary">Submit Button</button>