
<nav class="navbar-default navbar-static-side" role="navigation">
	<div class="sidebar-collapse">
		<ul class="nav" id="side-menu">
			
			<li><a href="#" class="dropdown-toggle" data-toggle="dropdown">Cadastros Básicos</a>
				<ul class="nav nav-second-level">
					<!-- MENU PARA DISTRICT -->
					<li><a href="#" class="dropdown-toggle" data-toggle="dropdown">Bairro<b class="caret"></b></a>
						<ul class="nav nav-third-level">
							<li><a href="#" onClick="loadPage('<g:createLink controller='District' action='create' />')"><span class="glyphicon glyphicon-plus"></span></span> Criar</a></li>
							<li><a href="#" onClick="loadPage('<g:createLink controller='District' action='index' />')"><span class="glyphicon glyphicon-list"></span> Listar</a></li>
						</ul>
					</li>
					
					<!-- MENU PARA STREET -->
					<li><a href="#" class="dropdown-toggle" data-toggle="dropdown">Rua<b class="caret"></b></a>
						<ul class="nav nav-third-level">
							<li><a href="#" onClick="loadPage('<g:createLink controller='Street' action='create' />')"><span class="glyphicon glyphicon-plus"></span> Criar</a></li>
							<li><a href="#" onClick="loadPage('<g:createLink controller='Street' action='index' />')"><span class="glyphicon glyphicon-list"></span> Listar</a></li>
						</ul>
					</li>
					<!-- MENU PARA BLOCK -->
					<li><a href="#" class="dropdown-toggle" data-toggle="dropdown">Quadra<b class="caret"></b></a>
						<ul class="nav nav-third-level">
							<li><a href="#" onClick="loadPage('<g:createLink controller='Block' action='create' />')"><span class="glyphicon glyphicon-plus"></span> Criar</a></li>
							<li><a href="#" onClick="loadPage('<g:createLink controller='Block' action='index' />')"><span class="glyphicon glyphicon-list"></span> Listar</a></li>
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
							<li><a href="#" onClick="loadPage('<g:createLink controller='Still' action='create' />')"><span class="glyphicon glyphicon-plus"></span> Criar</a></li>
							<li><a href="#" onClick="loadPage('<g:createLink controller='Still' action='index' />')"><span class="glyphicon glyphicon-list"></span> Listar</a></li>
						</ul>
					</li>
					<!-- MENU PARA USER -->
					<li><a href="#" class="dropdown-toggle" data-toggle="dropdown">Usuário<b class="caret"></b></a>
						<ul class="nav nav-third-level">
							<li><a href="#" onClick="loadPage('<g:createLink controller='User' action='create' />')"><span class="glyphicon glyphicon-plus"></span> Criar</a></li>
							<li><a href="#" onClick="loadPage('<g:createLink controller='User' action='index' />')"><span class="glyphicon glyphicon-list"></span> Listar</a></li>
						</ul>
					</li>
				</ul>
		</ul>
	</div>
</nav>
