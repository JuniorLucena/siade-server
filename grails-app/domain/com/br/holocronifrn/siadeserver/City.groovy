package com.br.holocronifrn.siadeserver

class City {
	
	String name
	static belongsTo = [state : State]
	static hasMany = [districty : Districty]
	
    static constraints = {
		name blank : false
    }
	
	@Override
	public String toString() {
		name
	}
}
