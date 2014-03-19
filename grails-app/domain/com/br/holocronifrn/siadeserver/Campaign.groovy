package com.br.holocronifrn.siadeserver

class Campaign {

	String name

	static hasMany = [user: User]

    static constraints = {
    	name blank: false
    }	
}
