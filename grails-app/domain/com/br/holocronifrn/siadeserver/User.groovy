	package com.br.holocronifrn.siadeserver

class User {

	transient springSecurityService

	String username
	String password
	boolean enabled = true
	boolean accountExpired
	boolean accountLocked
	boolean passwordExpired
	String name
	String code
	char gender
	String phone
	String cell
	Address address


	static transients = ['springSecurityService']

	static constraints = {
		username blank: false, unique: true
		password blank: false
		name blank: false, nullable: false
		code blank: false, nullable: false
		gender blank: true
		phone blank: true, nullable: true
		cell blank: true, nullable: true
	}

	static mapping = {
		password column: '`password`'
	}

	Set<UserLevel> getAuthorities() {
		UserUserLevel.findAllByUser(this).collect { it.userLevel } as Set
	}

	def beforeInsert() {
		encodePassword()
	}

	def beforeUpdate() {
		if (isDirty('password')) {
			encodePassword()
		}
	}

	protected void encodePassword() {
		password = springSecurityService.encodePassword(password)
	}
}
