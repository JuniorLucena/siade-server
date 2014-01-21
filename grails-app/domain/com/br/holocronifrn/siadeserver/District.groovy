package com.br.holocronifrn.siadeserver

class District {
	
	String name
	
	static belongsTo = [city : City]
	static hasMany = [blocks : Block]

    static constraints = {
		name blank : false
    }
	
	@Override
	public String toString() {
		name
	}
}
