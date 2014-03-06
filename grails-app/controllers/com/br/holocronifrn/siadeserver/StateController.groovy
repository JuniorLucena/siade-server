package com.br.holocronifrn.siadeserver



import static org.springframework.http.HttpStatus.*
import grails.plugin.springsecurity.annotation.Secured
import grails.transaction.Transactional

@Secured (['ROLE_ADMIN', 'ROLE_USER'])
@Transactional(readOnly = true)
class StateController {

}