package com.br.holocronifrn.siadeserver

import grails.converters.JSON
import grails.plugin.springsecurity.annotation.Secured

@Secured (['ROLE_ADMIN'])
class CityController {

	static scaffold = true
	
	def listCityState() {
		render City.findAllByStateLike(State.get(params.idState)) as JSON
	}
	
}
