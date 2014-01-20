package com.br.holocronifrn.siadeserver

class Districty {
	
	String name
	
	static belongsTo = [city : City]
	static hasMany = []

    static constraints = {
		name blank : false
    }
	
	@Override
	public String toString() {
		name
	}
}
