package com.br.holocronifrn.siadeserver



import static org.springframework.http.HttpStatus.*
import grails.converters.JSON
import grails.plugin.springsecurity.annotation.Secured
import grails.transaction.Transactional

@Secured (['ROLE_ADMIN'])
@Transactional(readOnly = true)
class StateController {

	static allowedMethods = [save: "POST", update: "POST", delete: "DELETE"]

	def index(Integer max) {
		params.max = Math.min(max ?: 10, 100)
		respond State.list(params), model:[stateInstanceCount: State.count()]
	}


	def show(State stateInstance) {
		respond stateInstance
	}

	def create() {
		respond new State(params)
	}

	@Transactional
	def save(State stateInstance) {
		if (stateInstance == null) {
			notFound()
			return
		}

		if (stateInstance.hasErrors()) {
			respond stateInstance.errors, view:'create'
			return
		}

		stateInstance.save flush:true

		request.withFormat {
			form {
				flash.message = message(code: 'default.created.message', args: [
					message(code: 'stateInstance.label', default: 'State'),
					stateInstance.id
				])
				redirect stateInstance
			}
			'*' { respond stateInstance, [status: CREATED] }
		}
	}

	def edit(State stateInstance) {
		respond stateInstance
	}

	@Transactional
	def update(State stateInstance) {
		if (stateInstance == null) {
			notFound()
			return
		}

		if (stateInstance.hasErrors()) {
			respond stateInstance.errors, view:'edit'
			return
		}

		stateInstance.save flush:true

		request.withFormat {
			form {
				flash.message = message(code: 'default.updated.message', args: [
					message(code: 'State.label', default: 'State'),
					stateInstance.id
				])
				redirect stateInstance
			}
			'*'{ respond stateInstance, [status: OK] }
		}
	}

	@Transactional
	def delete(State stateInstance) {

		if (stateInstance == null) {
			notFound()
			return
		}

		stateInstance.delete flush:true

		request.withFormat {
			form {
				flash.message = message(code: 'default.deleted.message', args: [
					message(code: 'State.label', default: 'State'),
					stateInstance.id
				])
				redirect action:"index", method:"GET"
			}
			'*'{ render status: NO_CONTENT }
		}
	}

	protected void notFound() {
		request.withFormat {
			form {
				flash.message = message(code: 'default.not.found.message', args: [
					message(code: 'stateInstance.label', default: 'State'),
					params.id
				])
				redirect action: "index", method: "GET"
			}
			'*'{ render status: NOT_FOUND }
		}
	}
}