package com.br.holocronifrn.siadeserver
import grails.plugin.springsecurity.annotation.Secured
import grails.converters.JSON

@Secured (['ROLE_ADMIN', 'ROLE_USER'])
class DistrictController {

   	static scaffold = true

   	def getDistricts() {
   		render District.list() as JSON
   	}
}
