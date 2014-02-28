package com.br.holocronifrn.siadeserver



import static org.springframework.http.HttpStatus.*
import grails.plugin.springsecurity.annotation.Secured
import grails.transaction.Transactional

@Secured (['ROLE_ADMIN'])
@Transactional(readOnly = true)
class StateController {

}