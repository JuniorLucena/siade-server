import groovy.json.JsonSlurper

import org.codehaus.groovy.grails.web.context.ServletContextHolder

import com.br.holocronifrn.siadeserver.City
import com.br.holocronifrn.siadeserver.State

static def init() {
	initStates()
	initCities()
}

static getPath(file) {
	ServletContextHolder.getServletContext().getRealPath("/WEB-INF/json/${file}")
}

static def getJSON(path) {
	def jsonSluper = new JsonSlurper()
	def reader = new BufferedReader(new FileReader(path))
	jsonSluper.parse(reader);
}

static def initCities() {
	def jsonCities = getJSON(getPath("Cidades.json"))
	jsonCities.each {c ->
		def city = new City([id: c.ID, name: c.Nome, state: State.get(c.Estado)]).save()
	}
}


static def initStates() {
	def jsonStates =  getJSON(getPath("Estados.json"))
	jsonStates.each { s ->
		def state = new State([id: s.ID, name: s.Nome,acronym: s.Sigla]).save()
	}
}