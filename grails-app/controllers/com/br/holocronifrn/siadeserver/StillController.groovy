package com.br.holocronifrn.siadeserver



import static org.springframework.http.HttpStatus.*
import grails.plugin.springsecurity.annotation.Secured
import grails.transaction.Transactional

@Secured (['ROLE_ADMIN'])
@Transactional(readOnly = true)
class StillController {

	static allowedMethods = [save: "POST", update: "PUT", delete: "DELETE"]

	def index(Integer max) {
		params.max = Math.min(max ?: 10, 100)
		respond Still.list(params), model:[stillInstanceCount: Still.count()]
	}

	def show(Still stillInstance) {
		respond stillInstance
	}

	def create() {
		respond new Still(params)
	}

	@Transactional
	def save(Still stillInstance) {
		if (stillInstance == null) {
			notFound()
			return
		}

		if (stillInstance.hasErrors()) {
			respond stillInstance.errors, view:'create'
			return
		}

		stillInstance.save flush:true

		request.withFormat {
			form {
				flash.message = message(code: 'default.created.message', args: [
					message(code: 'stillInstance.label', default: 'Still'),
					stillInstance.id
				])
				redirect stillInstance
			}
			'*' { respond stillInstance, [status: CREATED] }
		}
	}

	def edit(Still stillInstance) {
		respond stillInstance
	}

	@Transactional
	def update(Still stillInstance) {
		if (stillInstance == null) {
			notFound()
			return
		}

		if (stillInstance.hasErrors()) {
			respond stillInstance.errors, view:'edit'
			return
		}

		stillInstance.save flush:true

		request.withFormat {
			form {
				flash.message = message(code: 'default.updated.message', args: [
					message(code: 'Still.label', default: 'Still'),
					stillInstance.id
				])
				redirect stillInstance
			}
			'*'{ respond stillInstance, [status: OK] }
		}
	}

	@Transactional
	def delete(Still stillInstance) {

		if (stillInstance == null) {
			notFound()
			return
		}

		stillInstance.delete flush:true

		request.withFormat {
			form {
				flash.message = message(code: 'default.deleted.message', args: [
					message(code: 'Still.label', default: 'Still'),
					stillInstance.id
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
					message(code: 'stillInstance.label', default: 'Still'),
					params.id
				])
				redirect action: "index", method: "GET"
			}
			'*'{ render status: NOT_FOUND }
		}
	}
}
