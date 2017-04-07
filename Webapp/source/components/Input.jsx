import React, { Component } from 'react';

import validator from 'validator';
import classNames from 'classnames';

class Input extends Component {
    constructor(props){
	super(props);

	this.state = {
	    validation: true,
	    value: this.props.value || ''
	};

	this.handleChange = this.handleChange.bind(this);

    }

    validation(value){
	const validations = this.props.validation.split(",");
	const results = [];
	
	for (const index in validations){
	    const val  = validator[validations[index]](value);
	    results.push((validations[index] != 'isEmpty') ? val : !val);
	}

	this.setState({
	    validation: !results.includes(false)
	});
    }

    componentDidMount(){
	if (typeof this.props.validation !== 'undefined')
	    this.validation(this.state.value);
    }

    handleChange(event){
	if (typeof this.props.validation !== 'undefined')
	    this.validation(event.target.value);

	this.setState({
	    value: event.target.value
	});
    }

    render(){
	const rest = Object.assign({}, this.props);
	delete rest.validation;

	const classesGroup = classNames({
	    'form-group': true,
	    'has-error': !this.state.validation
	});

	return (
	    <div className={classesGroup}>
		<label htmlFor={this.props.id}>{this.props.placeholder}</label>
		<input {...rest} value={this.state.value} onChange={this.handleChange} data-validation={this.state.validation}/>
	    </div>
	);
    }
}

export default Input;
