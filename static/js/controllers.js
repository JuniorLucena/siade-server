'use strict'
var siadeCtrls = angular.module('siadeControllers', []);
      

siadeCtrls.controller('loginController', ['$scope', '$location', 'authService', function ($scope, $location, authService) {
 
}])

siadeCtrls.controller('homeCtrl', ['$scope', function($scope) {
	$scope.valor = 1
}])

siadeCtrls.controller('bairroCtrl', ['$scope', '$http', '$window', '$location', function($scope,$http,$window,$location) {

	$scope.addBairro = function(){
		$location.path('/cadastrar_bairro/')
	}
	
	$scope.editUf = function(bairro){
		$location.path('/edit_bairro/'+ bairro)
	}	
	
 	
	var init = function(){
		$http.get('/api/imoveis/bairro')
		.success(function (data){
			$scope.lista = data
		}).error(function(data){
			alert("erro no angularjs!")		
		})
 	   
	}
	
	init();
      
}])

siadeCtrls.controller('agenteCtrl', ['$scope', function($scope) {
	$scope.valor = 1
}])


siadeCtrls.controller('cidadeCtrl', ['$scope','$http', '$window', '$location', function ($scope,$http,$window,$location) {
	
	$scope.addCidade = function(){
		$location.path('/cadastrar_cidade/')
	}
	
	$scope.editUf = function(municipio){
		$location.path('/edit_municipio/'+ municipio)
	}	
	
 	
	var init = function(){
		$http.get('/api/imoveis/municipio')
		.success(function (data){
			$scope.lista = data
		}).error(function(data){
			alert("erro no angularjs!")		
		})
 	   
	}
	
	init();
}])


siadeCtrls.controller('cidade_Cadastro_Ctrl', ['$scope','$http', '$location', function ($scope,$http,$location) {

	$scope.municipio ={};

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


	var init = function(){
		$http.get('/api/imoveis/municipio')
		.success(function (data){
			$scope.lista = data
		}).error(function(data){
			alert("erro no angularjs!")		
		})
 	   
	}
	
	init();
}])

.controller('quadraCtrl', ['$scope', '$location', function($scope,$location) {
	$scope.addImovel = function(){
		$location.path('/imoveis/')
	}
}])



.controller('imovelCtrl', ['$scope', function($scope) {
	$scope.valor = 1
}])


siadeCtrls.controller('estadoCtrl', ['$scope','$http', '$location', '$window', function ($scope,$http,$location,$window) {
	  
	  var load = function() {
            console.log('call load()...');
            $http.get('/api/imoveis/uf')
                    .success(function(data, status, headers, config) {
                        console.log(data)
                        $scope.ufs = data;
                        angular.copy($scope.ufs, $scope.copy);
                    });
        }

        load();

	$scope.addUf = function(){
		$location.path('/cadastrar_uf/')
	}

	$scope.editUf = function(index){
		console.log('call editUf()...')
		$location.path('/edit_uf/' + $scope.ufs[index].id);
	}

	$scope.excluir = function(uf){
		var confirm = $window.confirm('Tem certeza que deseja excluir o produto '+ uf+ '?');
		if(confirm){
			$http.delete('/api/imoveis/uf/'+uf).success(function(data){
				var index = $scope.lista.indexOf(uf);
				$scope.lista.splice(index, 1);
			});
		}
	};

}])


siadeCtrls.controller('estadoEditCtrl', ['$scope', '$location', '$http', function ($scope, $http, $location) {

      
      var load = function() {
            console.log('call load()...');
            $http.get('/api/imoveis/uf')
                    .success(function(data, status, headers, config) {
                        console.log(data)
                        $scope.ufs = data;
                        angular.copy($scope.ufs, $scope.copy);
                    });
        }

        load();

         $scope.uf = {};

        $scope.updateUf = function() {
            console.log('call updateUf');
            $http
			.put('/api/imoveis/uf/' + $scope.uf.id + $scope.uf)
			.success(function(data, status, headers, config) {
				if(!data.error) {
					showMessage('Registro salvo com exito', 'success');
					$location.path('/categorias');
				} else {
					showMessage(data.error, 'error');
				}
			}).error(function(data, status, headers, config) {
				showMessage($.i18n.prop('SaveError'), 'success');
			});

		}
         
}]);


siadeCtrls.controller('estado_Cadastro_Ctrl', ['$scope','$http', '$location', function ($scope,$http,$location) {
	$scope.uf ={};

	$scope.saveUf = function(){
		
		$http.post('/api/imoveis/uf/', $scope.uf)
		.success(function (data){
			alert("post ")
			$scope.lista.unshift(data)
		}).error(function(data){
			alert("erro no codigo!")		
		})
	
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


siadeCtrls.controller('logradouroCtrl', ['$scope','$http', '$location', function ($scope,$http,$location) {
	

	$scope.addLogradouro = function(){
		$location.path('/cadastrar_logradouro/')
	}
		
	var init = function(){
		$http.get('/api/imoveis/logradouro')
		.success(function (data){
			$scope.lista = data
		}).error(function(data){
			alert("erro no angularjs!")		
		})
 	   
	}
	
	init();

}])

