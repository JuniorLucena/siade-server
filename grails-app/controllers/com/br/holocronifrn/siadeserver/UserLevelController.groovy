package com.br.holocronifrn.siadeserver



import static org.springframework.http.HttpStatus.*
import grails.transaction.Transactional

@Transactional(readOnly = true)
class UserLevelController {

    static allowedMethods = [save: "POST", update: "PUT", delete: "DELETE"]

    def index(Integer max) {
        params.max = Math.min(max ?: 10, 100)
        respond UserLevel.list(params), model:[userLevelInstanceCount: UserLevel.count()]
    }

    def show(UserLevel userLevelInstance) {
        respond userLevelInstance
    }

    def create() {
        respond new UserLevel(params)
    }

    @Transactional
    def save(UserLevel userLevelInstance) {
        if (userLevelInstance == null) {
            notFound()
            return
        }

        if (userLevelInstance.hasErrors()) {
            respond userLevelInstance.errors, view:'create'
            return
        }

        userLevelInstance.save flush:true

        request.withFormat {
            form {
                flash.message = message(code: 'default.created.message', args: [message(code: 'userLevelInstance.label', default: 'UserLevel'), userLevelInstance.id])
                redirect userLevelInstance
            }
            '*' { respond userLevelInstance, [status: CREATED] }
        }
    }

    def edit(UserLevel userLevelInstance) {
        respond userLevelInstance
    }

    @Transactional
    def update(UserLevel userLevelInstance) {
        if (userLevelInstance == null) {
            notFound()
            return
        }

        if (userLevelInstance.hasErrors()) {
            respond userLevelInstance.errors, view:'edit'
            return
        }

        userLevelInstance.save flush:true

        request.withFormat {
            form {
                flash.message = message(code: 'default.updated.message', args: [message(code: 'UserLevel.label', default: 'UserLevel'), userLevelInstance.id])
                redirect userLevelInstance
            }
            '*'{ respond userLevelInstance, [status: OK] }
        }
    }

    @Transactional
    def delete(UserLevel userLevelInstance) {

        if (userLevelInstance == null) {
            notFound()
            return
        }

        userLevelInstance.delete flush:true

        request.withFormat {
            form {
                flash.message = message(code: 'default.deleted.message', args: [message(code: 'UserLevel.label', default: 'UserLevel'), userLevelInstance.id])
                redirect action:"index", method:"GET"
            }
            '*'{ render status: NO_CONTENT }
        }
    }

    protected void notFound() {
        request.withFormat {
            form {
                flash.message = message(code: 'default.not.found.message', args: [message(code: 'userLevelInstance.label', default: 'UserLevel'), params.id])
                redirect action: "index", method: "GET"
            }
            '*'{ render status: NOT_FOUND }
        }
    }
}
