package com.br.holocronifrn.siadeserver

import grails.plugin.springsecurity.annotation.Secured

@Secured (['ROLE_ADMIN'])
class SecureController {
    
    def index () {
      render view: "/index"
   }
}
