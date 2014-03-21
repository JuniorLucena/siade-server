package com.br.holocronifrn.siadeserver



import static org.springframework.http.HttpStatus.*
import grails.converters.JSON
import grails.plugin.springsecurity.annotation.Secured
import grails.transaction.Transactional

@Secured (['ROLE_ADMIN'])
@Transactional(readOnly = true)
class SettingsController {
	
	def getCity() {
		return Settings.city
	}

	def getCitiesByStateId() {
		render City.findAllByStateLike(State.get(params.idState)) as JSON
	}

    static allowedMethods = [save: "POST", update: "PUT", delete: "DELETE"]

    def index(Integer max) {
        params.max = Math.min(max ?: 10, 100)
        respond Settings.list(params), model:[settingsInstanceCount: Settings.count()]
    }

    def show(Settings settingsInstance) {
        respond settingsInstance
    }

    def create() {
        respond new Settings(params)
    }

    @Transactional
    def save(Settings settingsInstance) {
        if (Settings.get(1) != null) {
            def settings = Settings.get(1)
            settings.state = settingsInstance.state
            settings.city = settingsInstance.city
            settings.save flush: true
            render "Dados Atualizados!"
        } else {
            settingsInstance.save flush:true
            render "Dados Salvos com sucesso!"
        }
    }

    def edit(Settings settingsInstance) {
        respond settingsInstance
    }

    @Transactional
    def update(Settings settingsInstance) {
        if (settingsInstance == null) {
            notFound()
            return
        }

        if (settingsInstance.hasErrors()) {
            respond settingsInstance.errors, view:'edit'
            return
        }

        settingsInstance.save flush:true

        request.withFormat {
            form {
                flash.message = message(code: 'default.updated.message', args: [message(code: 'Settings.label', default: 'Settings'), settingsInstance.id])
                redirect settingsInstance
            }
            '*'{ respond settingsInstance, [status: OK] }
        }
    }

    @Transactional
    def delete(Settings settingsInstance) {

        if (settingsInstance == null) {
            notFound()
            return
        }

        settingsInstance.delete flush:true

        request.withFormat {
            form {
                flash.message = message(code: 'default.deleted.message', args: [message(code: 'Settings.label', default: 'Settings'), settingsInstance.id])
                redirect action:"index", method:"GET"
            }
            '*'{ render status: NO_CONTENT }
        }
    }

    protected void notFound() {
        request.withFormat {
            form {
                flash.message = message(code: 'default.not.found.message', args: [message(code: 'settingsInstance.label', default: 'Settings'), params.id])
                redirect action: "index", method: "GET"
            }
            '*'{ render status: NOT_FOUND }
        }
    }
}






