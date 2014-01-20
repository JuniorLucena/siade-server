package com.br.holocronifrn.siadeserver

class State {

	String name
	String acronym
	
	static hasMany = [city : City]
	
    static constraints = {
		name blank : false 
		acronym blank : false, matches : /\w{2}/
    }
	
	@Override
	public String toString() {
		"$name - $acronym"
	}
	
}
