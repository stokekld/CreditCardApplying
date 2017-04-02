import React, { Component } from 'react';

import validator from 'validator';

class Input extends Component {
    constructor(props){
	super(props);
	
	this.state = {
	    inputProps: this.cleanProps(this.props),
	    validation: true,
	    value: this.props.value || ''
	};

	this.handleChange = this.handleChange.bind(this);

    }

    cleanProps(properties){

	const iP = Object.assign({}, this.props);
	delete iP.validation;
	return iP;

    }

    validation(value){
	console.log(this.state.value);
	const validations = this.props.validation.split(",");
	const results = [];
	
	for (const index in validations){
	    const val  = validator[validations[index]](this.state.value);
	    results.push((validations[index] != 'isEmpty') ? val : !val);

	    this.setState({
		validation: !results.includes(false)
	    });
	}
    }

    componentDidMount() {
	this.validation();
    }

    handleChange(event){
	this.setState({
	    value: event.target.value
	});

	this.validation();
    }

    render(){
	return (
	    <input {...this.state.inputProps} onChange={this.handleChange} data-eval={this.state.validation}/>
	);
    }
}

export default Input;
    //handleChange(event){
	//console.log(event.target.value);
	//console.log(this.props.validation);
	//console.log(validator[this.props.validation](event.target.value));

	//const validations = this.props.validation.split(",");

	//for (const index in validations){
	    //const validation = validations[ index ]

	    //if ( validation is 'isEmpty' )

	    //console.log(validator[validation](event.target.value));
	    //console.log(validations[ validation ]);
	//}
	//this.handleChange = this.handleChange.bind(this);
