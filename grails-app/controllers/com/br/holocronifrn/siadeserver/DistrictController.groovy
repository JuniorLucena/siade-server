package com.br.holocronifrn.siadeserver
import grails.plugin.springsecurity.annotation.Secured

@Secured (['ROLE_ADMIN'])
class DistrictController {

   	static scaffold = true
}
