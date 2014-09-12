'use strict'
var siadeApp = angular.module('siadeApp', [
	'ngRoute',
	'siadeControllers',
	'ui.select2'
])
siadeApp.config(['$routeProvider', function($routeProvider) {
	$routeProvider

	.when('/', {
		templateUrl: DJANGO_STATIC_URL+'login.html',
		controller: 'loginController'
	})

	.when('/estados', {
		templateUrl: DJANGO_STATIC_URL+'partials/listar_uf.html',
		controller: 'estadoCtrl'
	})

	.when('/cadastrar_uf', {
		templateUrl: DJANGO_STATIC_URL+'partials/cadastrar_uf.html',
		controller: 'estado_Cadastro_Ctrl'
	})

	.when('/edit_uf/:id', {
		templateUrl: DJANGO_STATIC_URL+'partials/edit_uf.html',
		controller: 'estadoEditCtrl'
	})

	.when('/logradouros', {
		templateUrl: DJANGO_STATIC_URL+'partials/listar_logradouro.html',
		controller: 'logradouroCtrl'
	})
	.when('/edit_logradouro/:id', {
		templateUrl: DJANGO_STATIC_URL+'partials/edit_logradouro.html',
		controller: 'logradouroEditCtrl'
	})
	.when('/cadastrar_logradouro', {
		templateUrl: DJANGO_STATIC_URL+'partials/cadastrar_logradouro.html',
		controller: 'logradouro_Cadastro_Ctrl'
	})
	
	.when('/cidades', {
		templateUrl: DJANGO_STATIC_URL+'partials/listar_cidade.html',
		controller: 'cidadeCtrl'
	})

	.when('/cadastrar_cidade/', {
		templateUrl: DJANGO_STATIC_URL+'partials/cadastrar_cidade.html',
		controller: 'cidade_Cadastro_Ctrl'
	})
	.when('/edit_municipio/:id', {
		templateUrl: DJANGO_STATIC_URL+'partials/edit_municipio.html',
		controller: 'cidadeEditCtrl'
	})

	.when('/bairros', {
		templateUrl: DJANGO_STATIC_URL+'partials/listar_bairro.html',
		controller: 'bairroCtrl'
	})
	.when('/edit_bairro/:id', {
		templateUrl: DJANGO_STATIC_URL+'partials/edit_bairro.html',
		controller: 'bairroEditCtrl'
	})

	.when('/cadastrar_bairro', {
		templateUrl: DJANGO_STATIC_URL+'partials/cadastrar_bairro.html',
		controller: 'bairro_Cadastro_Ctrl'
	})

	.when('/listar_quadras', {
		templateUrl: DJANGO_STATIC_URL+'partials/listar_quadra.html',
		controller: 'quadraCtrl'
	})
	.when('/edit_quadra/:id', {
		templateUrl: DJANGO_STATIC_URL+'partials/edit_quadra.html',
		controller: 'quadraEditCtrl'
	})

	.when('/cadastrar_quadras', {
		templateUrl: DJANGO_STATIC_URL+'partials/cadastrar_quadra.html',
		controller: 'cadastrar_quadra_Ctrl'
	})

	.when('/tipo-imovel', {
		templateUrl: DJANGO_STATIC_URL+'partials/listar_tipo_imovel.html',
		controller: 'tipoImovelCtrl'
	})

	.when('/cadastrar_tipo_imovel', {
		templateUrl: DJANGO_STATIC_URL+'partials/cadastrar_tipo_imovel.html',
		controller: 'tipoImovel_Cadastro_Ctrl'
	})
	.when('/imovel', {
		templateUrl: DJANGO_STATIC_URL+'partials/listar_imovel.html',
		controller: 'ImovelCtrl'
	})

	.when('/cadastrar_imovel', {
		templateUrl: DJANGO_STATIC_URL+'partials/cadastrar_imovel.html',
		controller: 'Imovel_Cadastro_Ctrl'
	})
	.when('/lado_quadra', {
		templateUrl: DJANGO_STATIC_URL+'partials/listar_lado_quadra.html',
		controller: 'lado_quadraCtrl'
	})

	.when('/cadastrar_lado_quadra', {
		templateUrl: DJANGO_STATIC_URL+'partials/cadastrar_lado_quadra.html',
		controller: 'ladoQuadra_Cadastro_Ctrl'
	})

	.when('/agentes', {
		templateUrl: DJANGO_STATIC_URL+'partials/listar_agentes.html',
		controller: 'agenteCtrl'
	})
	.when('/edit_agente/:id', {
		templateUrl: DJANGO_STATIC_URL+'partials/edit_agente.html',
		controller: 'agenteEditCtrl'
	})
	.when('/cadastrar_agente', {
		templateUrl: DJANGO_STATIC_URL+'partials/cadastrar_agente.html',
		controller: 'Agente_Cadastro_Ctrl'
	})

	.when('/atividades', {
		templateUrl: DJANGO_STATIC_URL+'partials/listar_atividade.html',
		controller: 'atividadeCtrl'
	})
	.when('/cadastrar_atividade', {
		templateUrl: DJANGO_STATIC_URL+'partials/cadastrar_atividade.html',
		controller: 'Atividade_Cadastro_Ctrl'
	})

	.when('/cadastrar_ciclo', {
		templateUrl: DJANGO_STATIC_URL+'partials/cadastrar_ciclo.html',
		controller: 'cadastrar_ciclo_Ctrl'
	})

	.when('/gerenciar_ciclo', {
		templateUrl: DJANGO_STATIC_URL+'partials/gerenciar_ciclo.html',
		controller: 'gerenciar_cicloCtrl'
	})

	.when('/relatorioD7', {
		templateUrl: DJANGO_STATIC_URL+'partials/relatorio_d7.html',
		controller: 'relatorio_d7'
	})

	.when('/relatorioD1', {
		templateUrl: DJANGO_STATIC_URL+'partials/relatorio_d1.html',
		controller: 'relatorio_d1'
	})

	.when('/relatorioCiclo', {
		templateUrl: DJANGO_STATIC_URL+'partials/relatorio_ciclo.html',
		controller: 'relatorio_ciclo'
	})

	.when('/relatorioPendente', {
		templateUrl: DJANGO_STATIC_URL+'partials/relatorio_pendente.html',
		controller: 'relatorio_pendente'

	})

  
    .otherwise({ redirectTo: "/index" })

   	//$httpProvider.defaults.headers.common['X-CSRFToken'] = $cookies.csrftoken


}])


siadeApp.config(['$httpProvider', function($httpProvider) {
	$httpProvider.defaults.xsrfCookieName = 'csrftoken';
	$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}])


 siadeApp.directive('calendar', function () {
            return {
                require: 'ngModel',
                link: function (scope, el, attr, ngModel) {
                    $(el).datepicker({
                        dateFormat: 'yy-mm-dd',
                        onSelect: function (dateText) {
                            scope.$apply(function () {
                                ngModel.$setViewValue(dateText);
                            });
                        }
                    });
                }
            };
        })


//myApp.factory('myService', function() {});

function cadastrar_ciclo_Ctrl($scope) {
    //$scope.name = 'Superhero';
}



