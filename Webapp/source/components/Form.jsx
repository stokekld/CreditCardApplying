import React, { Component } from 'react';
import ReactDOM, { findDOMNode } from 'react-dom';
import serialize from 'form-serialize';

import CreditApi from '../utils/Request.js';
import Input from './Input.jsx';
import ToastMsg from '../utils/Toast.js';


class Form extends Component {
    constructor(props){
	super(props);

	this.toast = new ToastMsg();
	this.request = new CreditApi();

	this.handleSubmit = this.handleSubmit.bind(this);

    }

    formValidation(){
	const evals = [];
	const inputs = findDOMNode(this).getElementsByTagName("input");

	for (let index = 0; index < inputs.length; index++)
	    evals.push(inputs[index].dataset.validation == 'true');
	
	return !evals.includes(false);
    }

    async handleSubmit(event){
	event.preventDefault();

	if (this.formValidation()){
	    const formData = serialize(event.target, { hash: true });

	    const data = await this.request.getData(this.props.endPoint, formData, this.props.method);

	    if (data.error)
		return;

	    this.props.trigger(data.response, data.status, this.toast);
	}

    }

    render(){
	return(
	    <form onSubmit={this.handleSubmit} autoComplete="off">
		<div>
		    {this.props.children}
		</div>
	    </form>
	);
    }

}

export default Form;
