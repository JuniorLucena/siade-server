package com.br.holocronifrn.siadeserver
import grails.plugin.springsecurity.annotation.Secured
import grails.converters.JSON

@Secured (['ROLE_ADMIN', 'ROLE_USER'])
class StreetController {
	
	static scaffold = true

	def getDistricts() {
   		render Street.list() as JSON
   	}

}
