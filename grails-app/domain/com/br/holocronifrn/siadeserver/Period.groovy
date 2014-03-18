package com.br.holocronifrn.siadeserver

class Period {

	Date startDate
	Date endDate
	Integer number
	Integer baseYear

	static hasMany = [users: User]

    static constraints = {
    	startDate blank: false
    	endDate blank: false
    	number blank: false
    	baseYear blank: false
    	users blank: false
    }
}
