package com.br.holocronifrn.siadeserver

class Address {

	String street
	String number
    String complement
    String district
    
    
    static constraints = {
    	street blank: false
    	number blank: false
    	district blank: false
    }
}
