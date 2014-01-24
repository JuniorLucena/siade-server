package com.br.holocronifrn.siadeserver

class Side {
	
	String reference
	Integer number
	
	static belongsTo = [street : Street, block : Block]
		
    static constraints = {
		number blank:false 
    }
	
	@Override
	public String toString() {
		number
	}
}
