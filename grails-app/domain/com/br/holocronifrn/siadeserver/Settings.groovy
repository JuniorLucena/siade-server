package com.br.holocronifrn.siadeserver

class Settings {

	static belongsTo = [state: State, city: City]
	
    static constraints = {
		state unique: true
		city unique: true
    }

    def getCity() {
    	Settings.findAllByCity()
    }
}
