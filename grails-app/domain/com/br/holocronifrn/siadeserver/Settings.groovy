package com.br.holocronifrn.siadeserver

class Settings {

	State state
	City city
	
    static constraints = {
		state unique: true
		city unique: true
    }
}
