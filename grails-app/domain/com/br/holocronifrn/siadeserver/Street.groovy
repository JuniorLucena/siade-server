package com.br.holocronifrn.siadeserver

class Street {
	
	String name
	
	static hasMany = [sides : Side]

    static constraints = {
		name blank:false 
    }
	
	@Override
	public String toString() {
		name
	}
}
