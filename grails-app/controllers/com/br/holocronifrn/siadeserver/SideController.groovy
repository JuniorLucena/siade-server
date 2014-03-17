package com.br.holocronifrn.siadeserver



import static org.springframework.http.HttpStatus.*
import grails.transaction.Transactional
import grails.plugin.springsecurity.annotation.Secured

@Secured (['ROLE_ADMIN'])
@Transactional(readOnly = true)
class SideController {

    static allowedMethods = [save: "POST", update: "PUT", delete: "DELETE"]

    def index(Integer max) {
        params.max = Math.min(max ?: 10, 100)
        respond Side.list(params), model:[sideInstanceCount: Side.count()]
    }

    def show(Side sideInstance) {
        respond sideInstance
    }

    def create() {
        respond new Side(params)
    }

    @Transactional
    def save(Side sideInstance) {
        if (sideInstance == null) {
            notFound()
            return
        }

        if (sideInstance.hasErrors()) {
            respond sideInstance.errors, view:'create'
            return
        }

        sideInstance.save flush:true

        request.withFormat {
            form {
                flash.message = message(code: 'default.created.message', args: [message(code: 'sideInstance.label', default: 'Side'), sideInstance.id])
                redirect sideInstance
            }
            '*' { respond sideInstance, [status: CREATED] }
        }
    }

    def edit(Side sideInstance) {
        respond sideInstance
    }

    @Transactional
    def update(Side sideInstance) {
        if (sideInstance == null) {
            notFound()
            return
        }

        if (sideInstance.hasErrors()) {
            respond sideInstance.errors, view:'edit'
            return
        }

        sideInstance.save flush:true

        request.withFormat {
            form {
                flash.message = message(code: 'default.updated.message', args: [message(code: 'Side.label', default: 'Side'), sideInstance.id])
                redirect sideInstance
            }
            '*'{ respond sideInstance, [status: OK] }
        }
    }

    @Transactional
    def delete(Side sideInstance) {

        if (sideInstance == null) {
            notFound()
            return
        }

        sideInstance.delete flush:true

        request.withFormat {
            form {
                flash.message = message(code: 'default.deleted.message', args: [message(code: 'Side.label', default: 'Side'), sideInstance.id])
                redirect action:"index", method:"GET"
            }
            '*'{ render status: NO_CONTENT }
        }
    }

    protected void notFound() {
        request.withFormat {
            form {
                flash.message = message(code: 'default.not.found.message', args: [message(code: 'sideInstance.label', default: 'Side'), params.id])
                redirect action: "index", method: "GET"
            }
            '*'{ render status: NOT_FOUND }
        }
    }
}
