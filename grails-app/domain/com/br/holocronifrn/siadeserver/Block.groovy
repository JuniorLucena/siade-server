package com.br.holocronifrn.siadeserver

class Block {
	
	String identification
	
	static belongsTo = [districty : Districty]
	static hasMany = [side : Side]
	

    static constraints = {
		identification blank:false 
    }
	
	@Override
	public String toString() {
		identification
	}
}
