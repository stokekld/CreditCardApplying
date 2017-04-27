import React, { Component } from 'react';

import classNames from 'classnames';
import Validation from '../utils/Validation.js';

class Input extends Component {
    constructor(props){
	super(props);

	this.state = {
	    validation: true,
	    value: this.props.value || ''
	};

	this.validation = new Validation(this.props.validation || '');

	this.handleChange = this.handleChange.bind(this);
    }

    componentDidMount(){
	this.setState({
	    validation: this.validation.validate(this.state.value)
	});
    }

    handleChange(event){
	this.setState({
	    validation: this.validation.validate(event.target.value),
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
		<input {...rest} className='form-control' value={this.state.value} onChange={this.handleChange} data-validation={this.state.validation}/>
	    </div>
	);
    }
}

export default Input;
