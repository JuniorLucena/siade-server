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