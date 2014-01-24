<!DOCTYPE html>
<html>
	<head>
		<meta name="layout" content="main" />
		<title>Welcome to Grails</title>
	</head>
	<body>
		<div class="container">
			<nav class="navbar navbar-default" role="navigation">
				<div class="navbar-header">
					<g:link class="navbar-brand">SIADE</g:link>
				</div>
				<div class="collapse navbar-collapse navbar-static-top" id="navmenu">
					<ul class="nav navbar-nav">
						<!-- MENU PARA CITY -->
						<li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">City<b class="caret"></b></a>
							<ul class="dropdown-menu">
								<li><g:link controller="city" action="create"><span class="glyphicon glyphicon-plus"></span> Create</g:link></li>
								<li><a href="#"><span class="glyphicon glyphicon-list"></span> List</a></li>
							</ul>
						</li>
						<!-- MENU PARA STATE -->
						<li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">State<b class="caret"></b></a>
							<ul class="dropdown-menu">
								<li><g:link controller="state" action="create"><span class="glyphicon glyphicon-plus"></span> Create</g:link></li>
								<li><a href="#"><span class="glyphicon glyphicon-list"></span> List</a></li>
							</ul>
						</li>
						<!-- MENU PARA DISTRICT -->
						<li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">District<b class="caret"></b></a>
							<ul class="dropdown-menu">
								<li><g:link controller="district" action="create"><span class="glyphicon glyphicon-plus"></span> Create</g:link></li>
								<li><a href="#"><span class="glyphicon glyphicon-list"></span> List</a></li>
							</ul>
						</li>
						<!-- MENU PARA STREET -->
						<li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">Street<b class="caret"></b></a>
							<ul class="dropdown-menu">
								<li><g:link controller="street" action="create"><span class="glyphicon glyphicon-plus"></span> Create</g:link></li>
								<li><a href="#"><span class="glyphicon glyphicon-list"></span> List</a></li>
							</ul>
						</li>
						<!-- MENU PARA BLOCK -->
						<li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">Block<b class="caret"></b></a>
							<ul class="dropdown-menu">
								<li><g:link controller="block" action="create"><span class="glyphicon glyphicon-plus"></span> Create</g:link></li>
								<li><a href="#"><span class="glyphicon glyphicon-list"></span> List</a></li>
							</ul>
						</li>
						<!-- MENU PARA SIDE -->
						<li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">Side<b class="caret"></b></a>
							<ul class="dropdown-menu">
								<li><g:link controller="side" action="create"><span class="glyphicon glyphicon-plus"></span> Create</g:link></li>
								<li><a href="#"><span class="glyphicon glyphicon-list"></span> List</a></li>
							</ul>
						</li>
						<!-- MENU PARA STILL -->
						<li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">Still<b class="caret"></b></a>
							<ul class="dropdown-menu">
								<li><g:link controller="still" action="create"><span class="glyphicon glyphicon-plus"></span> Create</g:link></li>
								<li><a href="#"><span class="glyphicon glyphicon-list"></span> List</a></li>
							</ul>
						</li>
					</ul>
				</div>
			</nav>
		</div>
	</body>
</html>
