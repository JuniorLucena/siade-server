package com.br.holocronifrn.siadeserver

class Block {
	
	String identification
	
	static belongsTo = [district : District]
	static hasMany = [side : Side]
	

    static constraints = {
		identification blank:false, matches : /\d+(\/\d+)?/
    }
	
	@Override
	public String toString() {
		identification
	}
}
