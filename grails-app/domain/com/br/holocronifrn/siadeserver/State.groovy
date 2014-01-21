package com.br.holocronifrn.siadeserver

class State {

	String name
	String acronym
	
	static hasMany = [cities : City]
	
    static constraints = {
		name blank : false 
		acronym blank : false, matches : /[A-Z]{2}/
    }
	
	@Override
	public String toString() {
		"$name - $acronym"
	}
	
}
