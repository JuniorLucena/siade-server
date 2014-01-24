package com.br.holocronifrn.siadeserver

class Side {
	
	String reference
	String number
	
	static belongsTo = [street : Street, block : Block]
		
    static constraints = {
    	reference blank:false
		number blank:false 
    }
	
	@Override
	public String toString() {
		number
	}
}
