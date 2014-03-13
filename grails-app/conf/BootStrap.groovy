import org.codehaus.groovy.grails.commons.GrailsApplication

import com.br.holocronifrn.siadeserver.Block
import com.br.holocronifrn.siadeserver.City
import com.br.holocronifrn.siadeserver.District
import com.br.holocronifrn.siadeserver.Side
import com.br.holocronifrn.siadeserver.State
import com.br.holocronifrn.siadeserver.Street
import com.br.holocronifrn.siadeserver.User
import com.br.holocronifrn.siadeserver.UserLevel
import com.br.holocronifrn.siadeserver.UserUserLevel

class BootStrap {

	GrailsApplication grailsApplication

	def init = { servletContext ->

		def adminUserLevel = new UserLevel(authority: 'ROLE_ADMIN').save(flush: true)
		def userUserLevel = new UserLevel(authority: 'ROLE_USER').save(flush: true)

		def testUser = new User(username: 'admin', password: 'pass', name:'administrador')
		testUser.save(flush: true)

		UserUserLevel.create testUser, adminUserLevel, true

		assert User.count() == 1
		assert UserLevel.count() == 2
		assert UserUserLevel.count() == 1

		/*inicializando os registros no banco de dados*/
		
		//inicializa todos os estados e cidades do Brazil
		InitializeStatesAndCities.init()

		District district1 = new District(name: "Chico Cajá", city : City.get(3783)).save(flush: true)
		Street street1 = new Street(name: "Planalt0 1").save(flush: true)
		Block block1 = new Block(identification: "1", district: district1).save(flush: true)
		Side side1 = new Side(reference: "prox. a X", number: 12, street: street1, block: block1).save(flush: true)
	}
}


