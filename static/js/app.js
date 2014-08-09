'use strict'
var siadeApp = angular.module('siadeApp', [
	'ngRoute',
	'siadeControllers'
])
siadeApp.config(['$routeProvider', function($routeProvider,$httpProvider) {
	$routeProvider
	$httpProvider.interceptors.push('authInterceptorService')

	
	.when('/index', {
		templateUrl: DJANGO_STATIC_URL + 'authentication/index.html',
		controller: 'indexController'
	})

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
	})
 
    .when("/login", {
        controller: "loginController",
        templateUrl: "authentication/login.html"
    })
 
    .when("/signup", {
        controller: "signupController",
        templateUrl: "authentication/signup.html"
    })
 
    .when("/orders", {
        controller: "ordersController",
        templateUrl: "authentication/orders.html"
    })
 
    .otherwise({ redirectTo: "/index" })

 //  	$httpProvider.defaults.headers.common['X-CSRFToken'] = $cookies.csrftoken


}])

siadeApp.run(['authService', function (authService) {
    authService.fillAuthData();
}])


