/*class BootStrap {

    def init = { servletContext ->
    }
    def destroy = {
    }
}
*/

import com.br.holocronifrn.siadeserver.User
import com.br.holocronifrn.siadeserver.UserLevel
import com.br.holocronifrn.siadeserver.UserUserLevel

class BootStrap {

   def init = { servletContext ->

      def adminUserLevel = new UserLevel(authority: 'ROLE_ADMIN').save(flush: true)
      def userUserLevel = new UserLevel(authority: 'ROLE_USER').save(flush: true)

      def testUser = new User(username: 'admin', password: 'pass')
      testUser.save(flush: true)

      UserUserLevel.create testUser, adminUserLevel, true

      assert User.count() == 1
      assert UserLevel.count() == 2
      assert UserUserLevel.count() == 1
   }
}


