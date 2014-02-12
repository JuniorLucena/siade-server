
<nav class="navbar-default navbar-static-side" role="navigation">
	<div class="sidebar-collapse">
		<ul class="nav" id="side-menu">
			<!-- MENU PARA CITY -->
			<li><a href="#" class="dropdown-toggle" data-toggle="dropdown">Cadastros Básicos</a>
				<ul class="nav nav-second-level">
					<li><a href="#" class="dropdown-toggle" data-toggle="dropdown">Cidade<b class="caret"></b></a>
						<ul class="nav nav-third-level">	
							<li><g:link controller="city" action="create"><span class="glyphicon glyphicon-plus"></span> Criar</g:link></li>
							<li><g:link controller="city" action="index"><span class="glyphicon glyphicon-list"></span> Listar</g:link></li>
						</ul>
					</li>
					<!-- MENU PARA STATE -->
					<li><a href="#" class="dropdown-toggle" data-toggle="dropdown">Estado<b class="caret"></b></a>
						<ul class="nav nav-third-level">
							<li><a href="#" onClick="loadPage('<g:createLink controller='State' action='create' />')"></span> Criar</a></li>
							<li><a href="#" onClick="loadPage('<g:createLink controller='State' action='index' />')"><span class="glyphicon glyphicon-list"></span> Listar</a></li>
						</ul>
					</li>
					<!-- MENU PARA DISTRICT -->
					<li><a href="#" class="dropdown-toggle" data-toggle="dropdown">Bairro<b class="caret"></b></a>
						<ul class="nav nav-third-level">
							<li><g:link controller="district" action="create" ><span class="glyphicon glyphicon-plus"></span> Criar</g:link></li>
							<li><g:link controller="district" action="index"><span class="glyphicon glyphicon-list"></span> Listar</g:link></li>
						</ul>
					</li>
					
					<!-- MENU PARA STREET -->
					<li><a href="#" class="dropdown-toggle" data-toggle="dropdown">Rua<b class="caret"></b></a>
						<ul class="nav nav-third-level">
							<li><g:link controller="street" action="create"><span class="glyphicon glyphicon-plus"></span> Criar</g:link></li>
							<li><g:link controller="street" action="index"><span class="glyphicon glyphicon-list"></span> Listar</g:link></li>
						</ul>
					</li>
					<!-- MENU PARA BLOCK -->
					<li><a href="#" class="dropdown-toggle" data-toggle="dropdown">Quadra<b class="caret"></b></a>
						<ul class="nav nav-third-level">
							<li><g:link controller="block" action="create"><span class="glyphicon glyphicon-plus"></span> Criar</g:link></li>
							<li><g:link controller="block" action="index"><span class="glyphicon glyphicon-list"></span> Listar</g:link></li>
						</ul>
					</li>
					<!-- MENU PARA SIDE -->
					<li ><a href="#" class="dropdown-toggle" data-toggle="dropdown">Lado<b class="caret"></b></a>
						<ul class="nav nav-third-level">
							<li><g:link controller="side" action="create"><span class="glyphicon glyphicon-plus"></span> Criar</g:link></li>
							<li><g:link controller="side" action="index"><span class="glyphicon glyphicon-list"></span> Listar</g:link></li>
						</ul>
					</li>
					<!-- MENU PARA STILL -->
					<li><a href="#" class="dropdown-toggle" data-toggle="dropdown">Imóvel<b class="caret"></b></a>
						<ul class="nav nav-third-level">
							<li><g:link controller="still" action="create"><span class="glyphicon glyphicon-plus"></span> Criar</g:link></li>
							<li><g:link controller="still" action="index"><span class="glyphicon glyphicon-list"></span> Listar</g:link></li>
						</ul>
					</li>
					
				</ul>
			</li>

			<!--BOTÂO LOGOUT-->
			<li><a href="j_spring_security_logout">Sair</a>
				
			</li>
		</ul>
	</div>
</nav>
