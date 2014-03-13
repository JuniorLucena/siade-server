package com.br.holocronifrn.siadeserver

class Agent {

	String name
	String code
	char gender
	String phone
	String cell
	Address address
	State state


	static belongsTo = [campaign: Campaign]

    static constraints = {
    	name blank:false
    	code blank:false
    	gender blank:false
    }
}
