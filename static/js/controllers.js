'use strict'
var siadeCtrls = angular.module('siadeControllers', []);
      

siadeCtrls.controller('loginController', ['$scope', '$location', function ($scope, $location) {
 
}])

siadeCtrls.controller('homeCtrl', ['$scope', function($scope) {
	$scope.valor = 1
}])


//lista Bairro

siadeCtrls.controller('bairroCtrl', ['$scope', '$http', '$window', '$location', function($scope,$http,$window,$location) {

	$scope.addBairro = function(){
		$location.path('/cadastrar_bairro/')
	}
	
	$scope.editBairro = function(index){
		console.log('call editBairro()...'+ $scope.bairros[index].id)
		$location.path('/edit_bairro/' + $scope.bairros[index].id);
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

        $scope.excluir = function(bairro){
			$http.delete('/api/imoveis/bairro/'+bairro).success(function(data){
				var index = $scope.bairros.indexOf(bairro);
				$scope.bairros.splice(index, 1);
			});
		
	};
      
}])

//editar Bairro...
siadeCtrls.controller('bairroEditCtrl', ['$scope', '$http','$routeParams', '$location', function ($scope, $http, $routeParams,$location) {
      
      var load = function() {
            console.log('load()... editBairro'+$routeParams.id)
            $http.get('/api/imoveis/bairro/'+$routeParams.id)
                    .success(function(data, status, headers, config) {
                        console.log(data)
                        $scope.bairros = data
                        angular.copy($scope.bairros, $scope.copy);
                    })
        }

        load()

         $scope.bairros = {};

        $scope.updateBairro = function() {
            console.log('updateBairro');
            $http
			.put('/api/imoveis/bairro/' + $scope.bairros.id , $scope.bairros)
			.success(function(data, status, headers, config) {
				if(!data.error) {
					$location.path('/bairros');
				} else {
					
				}
			}).error(function(data, status, headers, config) {
				
			});

		}

		 $http.get('/api/imoveis/municipio/')
			.success(function(data, status, headers, config) {
				$scope.municipios = data;
			});
         
}]);


//cadastrar Bairro...
siadeCtrls.controller('bairro_Cadastro_Ctrl', ['$scope','$http', '$location', function ($scope,$http,$location) {
	
	$scope.bairro ={};

	$scope.saveBairro = function(){
		
		$http.post('/api/imoveis/bairro/', $scope.bairro)
		.success(function (data){
			$scope.bairros.unshift(data)
			$location.path('/bairros')
		}).error(function(data){
					
		})
	
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

        
         $http.get('/api/imoveis/municipio/')
			.success(function(data, status, headers, config) {
				$scope.municipios = data;
			});


}])




//listar Agente
siadeCtrls.controller('agenteCtrl', ['$scope', '$http','$routeParams', '$location', function ($scope, $http, $routeParams,$location) {

	$scope.addAgente = function(){
		$location.path('/cadastrar_agente/')
	}
	
	$scope.editAgente = function(index){
		console.log('call editAgente()...'+ $scope.agentes[index].id)
		$location.path('/edit_agente/' + $scope.agentes[index].id);
	}

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

        $scope.excluir = function(agente){
			$http.delete('/api/trabalhos/agente/'+agente).success(function(data){
				var index = $scope.agentes.indexOf(agente);
				$scope.agentes.splice(index, 1);
			});
		
	};
}])

//editar Agente...
siadeCtrls.controller('agenteEditCtrl', ['$scope', '$http','$routeParams', '$location', function ($scope, $http, $routeParams,$location) {
      
      var load = function() {
            console.log('load()... editAgente'+$routeParams.id)
            $http.get('/api/trabalhos/agente/'+$routeParams.id)
                    .success(function(data, status, headers, config) {
                        console.log(data)
                        $scope.agentes = data
                        angular.copy($scope.agentes, $scope.copy);
                    })
        }

        load()

         $scope.agentes = {};

        $scope.updateAgente = function() {
            console.log('updateAgente');
            $http
			.put('/api/trabalhos/agente/' + $scope.agentes.id , $scope.agentes)
			.success(function(data, status, headers, config) {
				if(!data.error) {
					$location.path('/agentes');
				} else {
					
				}
			}).error(function(data, status, headers, config) {
				
			});

		}
         
}]);


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
	
	$scope.editCidade = function(index){
		console.log('call editCidade()...'+ $scope.municipios[index].id)
		$location.path('/edit_municipio/' + $scope.municipios[index].id);
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

        $scope.excluir = function(municipio){
			$http.delete('/api/imoveis/municipio/'+municipio).success(function(data){
				var index = $scope.municipios.indexOf(municipio);
				$scope.municipios.splice(index, 1);
			});
		
	};
}])

//editar Cidade...
siadeCtrls.controller('cidadeEditCtrl', ['$scope', '$http','$routeParams', '$location', function ($scope, $http, $routeParams,$location) {
      
      var load = function() {
            console.log('load()... editCidade'+$routeParams.id)
            $http.get('/api/imoveis/municipio/'+$routeParams.id)
                    .success(function(data, status, headers, config) {
                        console.log(data)
                        $scope.municipios = data
                        angular.copy($scope.municipios, $scope.copy);
                    })
        }

        load()

         $scope.municipios = {};

        $scope.updateCidade = function() {
            console.log('updateCidade');
            $http
			.put('/api/imoveis/municipio/' + $scope.municipios.id , $scope.municipios)
			.success(function(data, status, headers, config) {
				if(!data.error) {
					$location.path('/cidades');
				} else {
					
				}
			}).error(function(data, status, headers, config) {
				
			});

		}
         
}]);

//cadastrar Cidade...

siadeCtrls.controller('cidade_Cadastro_Ctrl', ['$scope','$http', '$location', function ($scope,$http,$location) {

	$scope.municipio ={};

	$scope.save = function(){
		
		$http.post('/api/imoveis/municipio/', $scope.municipio)
		.success(function (data){
			console.log(data)
			$location.path('/cidades')
			}).error(function(data){
				
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

         $http.get('/api/imoveis/uf/')
			.success(function(data, status, headers, config) {
				$scope.ufs = data;
			});
}])





//Listar Quadras

.controller('quadraCtrl', ['$scope', '$location', '$http', function($scope,$location, $http) {
	
	$scope.addQuadra = function(){
		$location.path('/cadastrar_quadras')
	}

	$scope.editQuadra = function(index){
		console.log('call editQuadra()...'+ $scope.quadras[index].id)
		$location.path('/edit_quadra/' + $scope.quadras[index].id);
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

        $scope.excluir = function(quadra){
			$http.delete('/api/imoveis/quadra/'+quadra).success(function(data){
				var index = $scope.quadras.indexOf(quadra);
				$scope.quadras.splice(index, 1);
			});
		
	};
}])

//editar Quadra...
siadeCtrls.controller('quadraEditCtrl', ['$scope', '$http','$routeParams', '$location', function ($scope, $http, $routeParams,$location) {
      
      var load = function() {
            console.log('load()... editQuadra'+$routeParams.id)
            $http.get('/api/imoveis/quadra/'+$routeParams.id)
                    .success(function(data, status, headers, config) {
                        console.log(data)
                        $scope.quadras = data
                        angular.copy($scope.quadras, $scope.copy);
                    })
        }

        load()

         $scope.quadras = {};

        $scope.updateQuadra = function() {
            console.log('updateQuadra');
            $http
			.put('/api/imoveis/quadra/' + $scope.quadras.id , $scope.quadras)
			.success(function(data, status, headers, config) {
				if(!data.error) {
					$location.path('/listar_quadras');
				} else {
					
				}
			}).error(function(data, status, headers, config) {
				
			});

		}
         
          $http.get('/api/imoveis/bairro/')
			.success(function(data, status, headers, config) {
				$scope.bairros = data;
			});
}]);
//Cadastrar Quadras

siadeCtrls.controller('cadastrar_quadra_Ctrl', ['$scope','$http', '$location', function ($scope,$http,$location) {

	$scope.quadra ={};

	$scope.saveQuadra = function(){
		
		$http.post('/api/imoveis/quadra/', $scope.quadra)
		.success(function (data){
			console.log(data)
			$location.path('/listar_quadras/')
			}).error(function(data){
			
		})
	
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

        $http.get('/api/imoveis/bairro/')
			.success(function(data, status, headers, config) {
				$scope.bairros = data;
			});
	
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
		console.log('call editUf()...'+ $scope.ufs[index].id)
		$location.path('/edit_uf/' + $scope.ufs[index].id);
	}

	$scope.excluir = function(uf){
			$http.delete('/api/imoveis/uf/'+uf).success(function(data){
				var index = $scope.ufs.indexOf(uf);
				$scope.ufs.splice(index, 1);
			});
		
	};

}])


//editar Estado...

siadeCtrls.controller('estadoEditCtrl', ['$scope', '$http','$routeParams', '$location', function ($scope, $http, $routeParams,$location) {
      
      var load = function() {
            console.log('load()... editUf'+$routeParams.id)
            $http.get('/api/imoveis/uf/'+$routeParams.id)
                    .success(function(data, status, headers, config) {
                        console.log(data)
                        $scope.ufs = data
                        angular.copy($scope.ufs, $scope.copy);
                    })
        }

        load()

         $scope.ufs = {};

        $scope.updateUf = function() {
            console.log('updateUf');
            $http
			.put('/api/imoveis/uf/' + $scope.ufs.id , $scope.ufs)
			.success(function(data, status, headers, config) {
				if(!data.error) {
					$location.path('/estados');
				} else {
					
				}
			}).error(function(data, status, headers, config) {
				
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

        load()


}])





//lista logradouro...

siadeCtrls.controller('logradouroCtrl', ['$scope','$http', '$location', function ($scope,$http,$location) {
	

	$scope.addLogradouro = function(){
		$location.path('/cadastrar_logradouro/')
	}
	$scope.editLogradouro = function(index){
		console.log('call editUf()...'+ $scope.logradouros[index].id)
		$location.path('/edit_logradouro/' + $scope.logradouros[index].id);
	}
		
	$scope.excluir = function(logradouro){
		
			$http.delete('/api/imoveis/logradouro/'+logradouro).success(function(data){
				var index = $scope.logradouros.indexOf(logradouro);
				$scope.logradouros.splice(index, 1);
			});
		
	};

	 var load = function() {
            console.log('call load()...');
            $http.get('/api/imoveis/logradouro')
                    .success(function(data, status, headers, config) {
                        console.log(data)
                        $scope.logradouros = data
                        angular.copy($scope.logradouros, $scope.copy)
                    })
        }

        load()

}])


// cadastro Logradouro...
siadeCtrls.controller('logradouro_Cadastro_Ctrl', ['$scope','$http', '$location', function ($scope,$http,$location) {
	
	$scope.logradouro ={};

	$scope.saveLogradouro = function(){
		
		$http.post('/api/imoveis/logradouro/', $scope.logradouro)
		.success(function (data){
			$scope.logradouros.unshift(data)
			$location.path('/logradouros')
		}).error(function(data){
			
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


         $http.get('/api/imoveis/municipio/')
			.success(function(data, status, headers, config) {
				$scope.municipios = data;
			});


}])

//editar Logradouro...
siadeCtrls.controller('logradouroEditCtrl', ['$scope', '$http','$routeParams', '$location', function ($scope, $http, $routeParams,$location) {
      
      var load = function() {
            console.log('load()... editLogradouro'+$routeParams.id)
            $http.get('/api/imoveis/logradouro/'+$routeParams.id)
                    .success(function(data, status, headers, config) {
                        console.log(data)
                        $scope.logradouros = data
                        angular.copy($scope.logradouros, $scope.copy);
                    })
        }

        load()

         $scope.logradouros = {};

        $scope.updateLogradouro = function() {
            console.log('updateLogradouro');
            $http
			.put('/api/imoveis/logradouro/' + $scope.logradouros.id , $scope.logradouros)
			.success(function(data, status, headers, config) {
				if(!data.error) {
					$location.path('/logradouros');
				} else {
					
				}
			}).error(function(data, status, headers, config) {
				
			});

		}

		 $http.get('/api/imoveis/municipio/')
			.success(function(data, status, headers, config) {
				$scope.municipios = data;
			});
         
}])

//Relatorios

siadeCtrls.controller('relatorio_d7', ['$scope', function($scope) {
	$scope.valor = 1
}])

siadeCtrls.controller('relatorio_d1', ['$scope', function($scope) {
	$scope.valor = 1
}])

siadeCtrls.controller('relatorio_ciclo', ['$scope', function($scope) {
	$scope.valor = 1
}])

siadeCtrls.controller('relatorio_pendente', ['$scope', function($scope) {
	$scope.valor = 1
}])


//Relatorios

siadeCtrls.controller('inicio_ciclo', ['$scope', function($scope) {
	$scope.valor = 1
}])
