package com.br.holocronifrn.siadeserver

import grails.plugin.springsecurity.annotation.Secured

@Secured (['ROLE_ADMIN', 'ROLE_USER'])
class CityController {
}
