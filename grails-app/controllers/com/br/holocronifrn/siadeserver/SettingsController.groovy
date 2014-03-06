package com.br.holocronifrn.siadeserver



import static org.springframework.http.HttpStatus.*
import grails.converters.JSON
import grails.plugin.springsecurity.annotation.Secured
import grails.transaction.Transactional

@Secured (['ROLE_ADMIN'])
@Transactional(readOnly = true)
class SettingsController {
	
	static scaffold = true
	
	def getCity() {
		return Settings.city
	}

	def getCitiesByStateId() {
		render City.findAllByStateLike(State.get(params.idState)) as JSON
	}
}
