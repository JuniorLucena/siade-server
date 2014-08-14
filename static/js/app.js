'use strict'
var siadeApp = angular.module('siadeApp', [
	'ngRoute',
	'siadeControllers',
	'ui.select2'
])
siadeApp.config(['$routeProvider', function($routeProvider) {
	$routeProvider

	.when('/', {
		templateUrl: DJANGO_STATIC_URL+'partials/home.html',
		controller: 'homeCtrl'
	})

	.when('/estados', {
		templateUrl: DJANGO_STATIC_URL+'partials/listar_uf.html',
		controller: 'estadoCtrl'
	})

	.when('/cadastrar_uf', {
		templateUrl: DJANGO_STATIC_URL+'partials/cadastrar_uf.html',
		controller: 'estado_Cadastro_Ctrl'
	})

	.when('/edit_uf', {
		templateUrl: DJANGO_STATIC_URL+'partials/edit_uf.html',
		controller: 'estadoCtrl'
	})

	.when('/logradouros', {
		templateUrl: DJANGO_STATIC_URL+'partials/listar_logradouro.html',
		controller: 'logradouroCtrl'
	})
	.when('/cadastrar_logradouro', {
		templateUrl: DJANGO_STATIC_URL+'partials/cadastrar_logradouro.html',
		controller: 'cadastrar_logradouro_Ctrl'
	})
	
	.when('/cidades', {
		templateUrl: DJANGO_STATIC_URL+'partials/listar_cidade.html',
		controller: 'cidadeCtrl'
	})

	.when('/cadastrar_cidade/', {
		templateUrl: DJANGO_STATIC_URL+'partials/cadastrar_cidade.html',
		controller: 'cidade_Cadastro_Ctrl'
	})

	.when('/bairros', {
		templateUrl: DJANGO_STATIC_URL+'partials/listar_bairro.html',
		controller: 'bairroCtrl'
	})

	.when('/cadastrar_bairro', {
		templateUrl: DJANGO_STATIC_URL+'partials/cadastrar_bairro.html',
		controller: 'cadastrar_bairro_Ctrl'
	})

	.when('/quadras', {
		templateUrl: DJANGO_STATIC_URL+'partials/quadra.html',
		controller: 'quadraCtrl'
	})

	.when('/imoveis', {
		templateUrl: DJANGO_STATIC_URL+'partials/imovel.html',
		controller: 'imovelCtrl'
	})
 
   

 
    .otherwise({ redirectTo: "/index" })

   	//$httpProvider.defaults.headers.common['X-CSRFToken'] = $cookies.csrftoken


}])


siadeApp.config(['$httpProvider', function($httpProvider) {
	$httpProvider.defaults.xsrfCookieName = 'csrftoken';
	$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}])