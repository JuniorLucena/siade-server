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
		respond Still.list(max: params.max, sort: "numberSequence", order: "asc"), model:[stillInstanceCount: Still.count()]
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


		realocateSequenceNumber(stillInstance)
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

	private void realocateSequenceNumber(realty) {	
		/* criteria responsável por pegar todos os objetos que tem o 
		 * numero de sequencia maior ou igual ao do imóvel, e que está no 
		 * mesmo lado, do imóvel comparado
		 */
		def realties = Still.withCriteria  {
			ge "numberSequence", realty.numberSequence
			like "side", realty.side
		}

		realties.each {
			it.numberSequence += 1
			it.save flush:true
		}
	}
}