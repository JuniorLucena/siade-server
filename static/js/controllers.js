'use strict'
var siadeCtrls = angular.module('siadeControllers', []);
      
siadeCtrls.controller('loginController', ['$scope', '$location', 'authService', function ($scope, $location, authService) {
 
    $scope.loginData = {
        userName: "",
        password: ""
    };
 
    $scope.message = "";
 
    $scope.login = function () {
 
        authService.login($scope.loginData).then(function (response) {
 
            $location.path('/orders');
 
        },
         function (err) {
             $scope.message = err.error_description;
         });
    };
 
}])

siadeCtrls.controller('homeCtrl', ['$scope', function($scope) {
	$scope.valor = 1
}])

siadeCtrls.controller('bairroCtrl', ['$scope', function($scope) {

}])

siadeCtrls.controller('cidadeCtrl', ['$scope','$http', '$window', function($scope, $http, $window) {
	$scope.municipio = {};

	$scope.save = function(){
		$http.post('/api/imoveis/municipio/', $scope.municipio)
		.success(function (data){
			console.log(data)
			}).error(function(data){
			alert("erro no angularjs!")		
		})	
	}
	
	$scope.edit = function(municipio){
		$window.console.log(municipio)
	}

	$http.get('/api/imoveis/municipio/')
		.success(function (data){
			console.log(data)
		}).error(function(data){
			alert("erro no angularjs!")		
		})

}])
.controller('quadraCtrl', ['$scope', function($scope) {
	$scope.valor = 1
}])
.controller('imovelCtrl', ['$scope', function($scope) {
	$scope.valor = 1
}])

siadeCtrls.controller('estadoCtrl', ['$scope','$http', '$location', function ($scope,$http,$location) {
	$scope.uf ={};

	
	$scope.saveUf = function(){
		
		$http.post('/api/imoveis/uf', $scope.uf)
		.success(function (data){
			$scope.lista.unshift(data)
		}).error(function(data){
			alert("erro no codigo!")		
		})
	
	}
	$scope.addUf = function(){
		$location.path('/cadastrar_uf/')
	}
	
	$scope.editUf = function(uf){
		$location.path('/edit_uf/'+ uf    		)
	}	
	
 	
	var init = function(){
		$http.get('/api/imoveis/uf')
		.success(function (data){
			$scope.lista = data
		}).error(function(data){
			alert("erro no angularjs!")		
		})
 	   
	}
	
	init();
}])

siadeCtrls.controller('indexController', ['$scope', '$location', 'authService', function ($scope, $location, authService) {
 
    $scope.logOut = function () {
        authService.logOut();
        $location.path('/home');
    }
 
    $scope.authentication = authService.authentication;
 
}])


siadeCtrls.controller('signupController', ['$scope', '$location', '$timeout', 'authService', function ($scope, $location, $timeout, authService) {
 
    $scope.savedSuccessfully = false;
    $scope.message = "";
 
    $scope.registration = {
        userName: "",
        password: "",
        confirmPassword: ""
    };
 
    $scope.signUp = function () {
 
        authService.saveRegistration($scope.registration).then(function (response) {
 
            $scope.savedSuccessfully = true;
            $scope.message = "User has been registered successfully, you will be redicted to login page in 2 seconds.";
            startTimer();
 
        },
         function (response) {
             var errors = [];
             for (var key in response.data.modelState) {
                 for (var i = 0; i < response.data.modelState[key].length; i++) {
                     errors.push(response.data.modelState[key][i]);
                 }
             }
             $scope.message = "Failed to register user due to:" + errors.join(' ');
         });
    };
 
    var startTimer = function () {
        var timer = $timeout(function () {
            $timeout.cancel(timer);
            $location.path('/index');
        }, 2000);
    }
 
}])
