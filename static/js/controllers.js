'use strict'
var siadeCtrls = angular.module('siadeControllers', []);
      
siadeCtrls.controller('homeCtrl', ['$scope', function($scope) {
	$scope.valor = 1
}])

siadeCtrls.controller('bairroCtrl', ['$scope', function($scope) {
	
      
}])

siadeCtrls.controller('cidadeCtrl', ['$scope','$http', '$window', function ($scope,$http,$window) {
	$scope.municipio ={};

	$scope.save = function(){
		
		$http.post('/api/imoveis/municipio', $scope.municipio)
		.success(function (data){
			console.log(data)
			}).error(function(data){
			alert("erro no angularjs!")		
		})
	
	}
	
	$scope.edit = function(municipio){
		$window.console.log(municipio)
	}	


$http.get('/api/imoveis/municipio')
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
