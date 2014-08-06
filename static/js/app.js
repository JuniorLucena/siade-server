'use strict'
var siadeApp = angular.module('siadeApp', [
	'ngRoute',
	'siadeControllers'
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
		controller: 'estadoCtrl'
	})
	.when('/edit_uf', {
		templateUrl: DJANGO_STATIC_URL+'partials/edit_uf.html',
		controller: 'estadoCtrl'
	})
	.when('/logradouros', {
		templateUrl: DJANGO_STATIC_URL+'partials/cadastrar_logradouro.html',
		controller: 'logradouroCtrl'
	})
	
	.when('/cidades', {
		templateUrl: DJANGO_STATIC_URL+'partials/cidade.html',
		controller: 'cidadeCtrl'
	})
	.when('/bairros', {
		templateUrl: DJANGO_STATIC_URL+'partials/bairro.html',
		controller: 'bairroCtrl'
	})
	.when('/quadras', {
		templateUrl: DJANGO_STATIC_URL+'partials/quadra.html',
		controller: 'quadraCtrl'
	})
	.when('/imoveis', {
		templateUrl: DJANGO_STATIC_URL+'partials/imovel.html',
		controller: 'imovelCtrl'
	})/*
	.otherwise({
		redirectTo: '/'
	})*/
}])
