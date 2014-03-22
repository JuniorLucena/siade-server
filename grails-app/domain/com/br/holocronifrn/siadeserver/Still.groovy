package com.br.holocronifrn.siadeserver

class Still {
	
	int habitants_amount
	int dogs_amount
	int cats_amount
	String still_number
	int numberSequence
	RealtyType idStillTipe

	static belongsTo = [side : Side]
	//static hasOne = [idStillTipe: RealtyType]

    static constraints = {
		habitants_amount blank:false
		dogs_amount blank:false
		cats_amount blank:false
		still_number blank:false
		//idStillTipe blank:false
		numberSequence blank:false
    }
	
	@Override
	public String toString() {
		"Imóvel número:  ${still_number}"	
	}
}
