import validator from 'validator';

class Validation{

    constructor(types){
	this.validations = types.split(",");
    }

    validate(value){
	const results = [];
	
	for (const index in this.validations){
	    const val  = validator[this.validations[index]](value);
	    results.push((this.validations[index] != 'isEmpty') ? val : !val);
	}

	return !results.includes(false);
    }
}

export default Validation;
