package com.br.holocronifrn.siadeserver

class Still {
	
	int habitants_amount
	int dogs_amount
	int cats_amount
	String still_number
	int idStillTipe

	static belongsTo = [side : Side]

    static constraints = {
		habitants_amount blank:false
		dogs_amount blank:false
		cats_amount blank:false
		still_number blank:false
		idStillTipe blank:false
    }
	
	@Override
	public String toString() {
		still_number	
	}
}
