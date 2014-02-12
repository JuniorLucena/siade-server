<!DOCTYPE html>
<html>

<head>

<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Siade - Controle de Endemias</title>

<!-- Core CSS - Include with every page -->
<link href="/siade-server/static/css/bootstrap.min.css" rel="stylesheet">
<link href="/siade-server/static/font-awesome/css/font-awesome.css"
	rel="stylesheet">

<!-- SB Admin CSS - Include with every page -->
<link href="/siade-server/static/css/sb-admin.css" rel="stylesheet">

</head>

<body>

	<div class="container">
		<div class="row">
			<div class="col-md-4 col-md-offset-4">
				<div class="login-panel panel panel-default">
					<div class="panel-heading">
						<h3 class="panel-title">Please Sign In</h3>
					</div>
					
					<div class="panel-body">
						<form role="form" method="POST"
							action="${resource(file: 'j_spring_security_check')}">
							<fieldset>
								<div class="form-group">
									<input class="form-control" placeholder="Username"
										name="j_username" type="text" autofocus>
								</div>
								<div class="form-group">
									<input class="form-control" placeholder="Password"
										name="j_password" type="password" value="">
								</div>
								<div class="checkbox">
									<label> <input name="_spring_security_remember_me"
										type="checkbox" value="Remember Me">Remember Me
									</label>
								</div>
								<!-- Change this to a button or input when using this as a form -->
								<g:submitButton name="="
									login" value='${message(code: "springSecurity.login.button")}'
									class="btn btn-lg btn-success btn-block">Login</g:submitButton>
							</fieldset>
						</form>
					</div>
				</div>
				
					<%--
					responsável por emitir a mensagem de erro
					--%>
					
					<g:if test='${flash.message}'>
						<div class='alert alert-danger'>
							${flash.message}
						</div>
					</g:if>
					
					
			</div>
		</div>
	</div>

	<!-- Core Scripts - Include with every page -->
	<script src="/siade-server/static/js/jquery-1.10.2.js"></script>
	<script src="/siade-server/static/js/bootstrap.min.js"></script>
	<script
		src="/siade-server/static/js/plugins/metisMenu/jquery.metisMenu.js"></script>

</body>

</html>
