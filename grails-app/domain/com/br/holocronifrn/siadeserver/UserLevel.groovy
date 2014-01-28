package com.br.holocronifrn.siadeserver

class UserLevel {

	String authority

	static mapping = {
		cache true
	}

	static constraints = {
		authority blank: false, unique: true
	}
}
