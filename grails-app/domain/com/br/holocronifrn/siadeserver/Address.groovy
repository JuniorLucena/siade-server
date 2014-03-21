package com.br.holocronifrn.siadeserver

class Address {

	
    Street street
    District district
 	String number
    String complement

    static constraints = {
    	
    	number blank: false
 
    }

    @Override
	public String toString() {
		street?.name
	}
}

