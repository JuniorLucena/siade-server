package com.br.holocronifrn.siadeserver

class RealtyType {
	
	String type
	
	//static belongsTo = [still : Still]

    static constraints = {
		type blank : false
    }
	
	@Override
	public String toString() {
		type
	}
}
