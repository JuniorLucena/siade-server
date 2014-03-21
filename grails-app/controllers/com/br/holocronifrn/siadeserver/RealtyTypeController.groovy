package com.br.holocronifrn.siadeserver



import static org.springframework.http.HttpStatus.*
import grails.transaction.Transactional

@Transactional(readOnly = true)
class RealtyTypeController {

    static allowedMethods = [save: "POST", update: "PUT", delete: "DELETE"]

    def index(Integer max) {
        params.max = Math.min(max ?: 10, 100)
        respond RealtyType.list(params), model:[realtyTypeInstanceCount: RealtyType.count()]
    }

    def show(RealtyType realtyTypeInstance) {
        respond realtyTypeInstance
    }

    def create() {
        respond new RealtyType(params)
    }

    @Transactional
    def save(RealtyType realtyTypeInstance) {
        if (realtyTypeInstance == null) {
            notFound()
            return
        }

        if (realtyTypeInstance.hasErrors()) {
            respond realtyTypeInstance.errors, view:'create'
            return
        }

        realtyTypeInstance.save flush:true

        request.withFormat {
            form {
                flash.message = message(code: 'default.created.message', args: [message(code: 'realtyTypeInstance.label', default: 'RealtyType'), realtyTypeInstance.id])
                redirect realtyTypeInstance
            }
            '*' { respond realtyTypeInstance, [status: CREATED] }
        }
    }

    def edit(RealtyType realtyTypeInstance) {
        respond realtyTypeInstance
    }

    @Transactional
    def update(RealtyType realtyTypeInstance) {
        if (realtyTypeInstance == null) {
            notFound()
            return
        }

        if (realtyTypeInstance.hasErrors()) {
            respond realtyTypeInstance.errors, view:'edit'
            return
        }

        realtyTypeInstance.save flush:true

        request.withFormat {
            form {
                flash.message = message(code: 'default.updated.message', args: [message(code: 'RealtyType.label', default: 'RealtyType'), realtyTypeInstance.id])
                redirect realtyTypeInstance
            }
            '*'{ respond realtyTypeInstance, [status: OK] }
        }
    }

    @Transactional
    def delete(RealtyType realtyTypeInstance) {

        if (realtyTypeInstance == null) {
            notFound()
            return
        }

        realtyTypeInstance.delete flush:true

        request.withFormat {
            form {
                flash.message = message(code: 'default.deleted.message', args: [message(code: 'RealtyType.label', default: 'RealtyType'), realtyTypeInstance.id])
                redirect action:"index", method:"GET"
            }
            '*'{ render status: NO_CONTENT }
        }
    }

    protected void notFound() {
        request.withFormat {
            form {
                flash.message = message(code: 'default.not.found.message', args: [message(code: 'realtyTypeInstance.label', default: 'RealtyType'), params.id])
                redirect action: "index", method: "GET"
            }
            '*'{ render status: NOT_FOUND }
        }
    }
}
