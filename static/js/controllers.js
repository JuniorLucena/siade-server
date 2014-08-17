'use strict'
var siadeCtrls = angular.module('siadeControllers', []);
      

siadeCtrls.controller('loginController', ['$scope', '$location', 'authService', function ($scope, $location, authService) {
 
}])

siadeCtrls.controller('homeCtrl', ['$scope', function($scope) {
	$scope.valor = 1
}])




//lista Bairro

siadeCtrls.controller('bairroCtrl', ['$scope', '$http', '$window', '$location', function($scope,$http,$window,$location) {

	$scope.addBairro = function(){
		$location.path('/cadastrar_bairro/')
	}
	
	$scope.editUf = function(bairro){
		$location.path('/edit_bairro/'+ bairro)
	}	
	
 	
	var load = function() {
            console.log('call load()...');
            $http.get('/api/imoveis/bairro')
                    .success(function(data, status, headers, config) {
                        console.log(data)
                        $scope.bairros = data;
                        angular.copy($scope.bairros, $scope.copy);
                    });
        }

        load();
      
}])

//cadastrar Bairro...

siadeCtrls.controller('bairro_Cadastro_Ctrl', ['$scope','$http', '$location', function ($scope,$http,$location) {

	$scope.bairro ={};

	$scope.saveBairro = function(){
		
		$http.post('/api/imoveis/bairro/', $scope.bairro)
		.success(function (data){
			$scope.bairros.unshift(data)
			
			$location.path('/bairros')
		}).error(function(data){
			alert("erro no codigo!")		
		})
	
	}
		
	 var load = function() {
            console.log('call cadastro load()...');
            $http.get('/api/imoveis/bairro')
                    .success(function(data, status, headers, config) {
                        console.log(data)
                        $scope.bairros = data;
                        angular.copy($scope.bairros, $scope.copy);
                    });
        }

        load();

         $http.get('/api/imoveis/municipio')
			.success(function(data, status, headers, config) {
				$scope.municipios = data;
			});

		
}])






//listar Agente
siadeCtrls.controller('agenteCtrl', ['$scope', function($scope) {
	var load = function() {
            console.log('call list load()...');
            $http.get('/api/trabalhos/agente')
                    .success(function(data, status, headers, config) {
                        console.log(data)
                        $scope.agentes = data;
                        angular.copy($scope.agentes, $scope.copy);
                    });
        }

        load();
}])

//cadastrar Agente

siadeCtrls.controller('Agente_Cadastro_Ctrl', ['$scope','$http', '$location', function ($scope,$http,$location) {

	$scope.agente ={};

	$scope.saveAgente = function(){
		
		$http.post('/api/trabalhos/agente/', $scope.agente)
		.success(function (data){
			$scope.agentes.unshift(data)
			showMessage('Save success')
			$location.path('/agentes')
		}).error(function(data){
			alert("erro no codigo!")		
		})
	
	}
		
	 var load = function() {
            console.log('call load()...');
            $http.get('/api/trabalhos/agente')
                    .success(function(data, status, headers, config) {
                        console.log(data)
                        $scope.agentes = data;
                        angular.copy($scope.agentes, $scope.copy);
                    });
        }

        load();

}])







//lista Cidade...
siadeCtrls.controller('cidadeCtrl', ['$scope','$http', '$window', '$location', function ($scope,$http,$window,$location) {
	
	$scope.addCidade = function(){
		$location.path('/cadastrar_cidade/')
	}
	
	$scope.editUf = function(municipio){
		$location.path('/edit_municipio/'+ municipio)
	}	
	
 	
	 var load = function() {
            console.log('call load()...');
            $http.get('/api/imoveis/municipio')
                    .success(function(data, status, headers, config) {
                        console.log(data)
                        $scope.municipios = data;
                        angular.copy($scope.municipios, $scope.copy);
                    });
        }

        load();
}])


//cadastrar Cidade...

siadeCtrls.controller('cidade_Cadastro_Ctrl', ['$scope','$http', '$location', function ($scope,$http,$location) {

	$scope.municipio ={};

	$scope.save = function(){
		
		$http.post('/api/imoveis/municipio/', $scope.municipio)
		.success(function (data){
			console.log(data)
			$location.path('/cidades')
			}).error(function(data){
			alert("erro no angularjs!")		
		})
	
	}

	 var load = function() {
            console.log('call load()...');
            $http.get('/api/imoveis/municipio')
                    .success(function(data, status, headers, config) {
                        console.log(data)
                        $scope.municipios = data;
                        angular.copy($scope.municipios, $scope.copy);
                    });
        }

        load();
}])





//Listar Quadras

.controller('quadraCtrl', ['$scope', '$location', '$http', function($scope,$location, $http) {
	
	$scope.addCidade = function(){
		$location.path('/cadastrar_quadras/')
	}

	var load = function() {
            console.log('call load()...');
            $http.get('/api/imoveis/quadra')
                    .success(function(data, status, headers, config) {
                        console.log(data)
                        $scope.quadras = data;
                        angular.copy($scope.quadras, $scope.copy);
                    });
        }

        load();
}])

//Cadastrar Quadras

siadeCtrls.controller('cadastrar_quadra_Ctrl', ['$scope','$http', '$location', function ($scope,$http,$location) {

	$scope.quadra ={};

	$scope.saveQuadra = function(){
		
		$http.post('/api/imoveis/quadra/add/', $scope.quadra)
		.success(function (data){
			console.log(data)
			//$location.path('/cadastrar_imoveis/')
			}).error(function(data){
			alert("erro no angularjs!")		
		})
	
	}
	
	$scope.edit = function(quadra){
		$window.console.log(quadra)
	}	


	var init = function(){
		$http.get('/api/imoveis/quadra/add')
		.success(function (data){
			$scope.lista = data
		}).error(function(data){
			alert("erro no angularjs!")		
		})
 	   
	}
	
	init();
}])






.controller('imovelCtrl', ['$scope', function($scope) {
	$scope.valor = 1
}])






//lista Estado...

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
				var index = $scope.ufs.indexOf(uf);
				$scope.ufs.splice(index, 1);
			});
		}
	};

}])


//editar Estado...

siadeCtrls.controller('estadoEditCtrl', ['$scope', '$location', '$http', '$routeParams', function ($scope, $http, $location,$routeParams) {
      
      var load = function() {
            console.log('call load()...');
            $http.get('/api/imoveis/uf'+$routeParams.id)
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
					$location.path('/estado_Cadastro_Ctrl');
				} else {
					showMessage(data.error, 'error');
				}
			}).error(function(data, status, headers, config) {
				showMessage($.i18n.prop('SaveError'), 'success');
			});

		}
         
}]);


//cadastrar Estado...


siadeCtrls.controller('estado_Cadastro_Ctrl', ['$scope','$http', '$location', function ($scope,$http,$location) {
	$scope.uf ={};

	$scope.saveUf = function(){
		
		$http.post('/api/imoveis/uf/', $scope.uf)
		.success(function (data){
			$scope.ufs.unshift(data)
			
			$location.path('/estados')
		}).error(function(data){
			alert("erro no codigo!")		
		})
	
	}
		
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


}])





//lista logradouro...

siadeCtrls.controller('logradouroCtrl', ['$scope','$http', '$location', function ($scope,$http,$location) {
	

	$scope.addLogradouro = function(){
		$location.path('/cadastrar_logradouro/')
	}
		
	$scope.excluir = function(logradouro){
		var confirm = $window.confirm('Tem certeza que deseja excluir o logradouro '+ logradouro+ '?');
		if(confirm){
			$http.delete('/api/imoveis/logradouro/'+logradouro).success(function(data){
				var index = $scope.logradouros.indexOf(logradouro);
				$scope.logradouros.splice(index, 1);
			});
		}
	};

	 var load = function() {
            console.log('call load()...');
            $http.get('/api/imoveis/logradouro')
                    .success(function(data, status, headers, config) {
                        console.log(data)
                        $scope.logradouros = data;
                        angular.copy($scope.logradouros, $scope.copy);
                    });
        }

        load();

}])


// cadastro Logradouro...
siadeCtrls.controller('logradouro_Cadastro_Ctrl', ['$scope','$http', '$location', function ($scope,$http,$location) {
	
	$scope.logradouro ={}

	$scope.saveLogradouro = function(){
		
		$http.post('/api/imoveis/logradouro/', $scope.uf)
		.success(function (data){
			alert("post ")
			$scope.logradouros.unshift(data)
		}).error(function(data){
			alert("erro no codigo!")		
		})
	
	}
		
	 var load = function() {
            console.log('call load()...');
            $http.get('/api/imoveis/logradouro')
                    .success(function(data, status, headers, config) {
                        console.log(data)
                        $scope.logradouros = data;
                        angular.copy($scope.logradouros, $scope.copy);
                    });
        }

        load();


}])


