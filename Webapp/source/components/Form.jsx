import React, { Component } from 'react';
import serialize from 'form-serialize';

import CreditApi from '../utils/Request.js';
import Input from './Input.jsx';
import ToastMsg from '../utils/Toast.js';


class Form extends Component {
    constructor(props){
	super(props);

	this.state = {
	    success: false
	};

	this.toast = new ToastMsg();

	this.handleSubmit = this.handleSubmit.bind(this);
    }

    async handleSubmit(event){
	event.preventDefault();

	const evals = [];

	for (const key in this.refs)
	    evals.push(this.refs[key].state.validation);

	const validation = !evals.includes(false);
	
	if (validation){
	    const formData = serialize(event.target, { hash: true });

	    const request = new CreditApi();
	    const data = await request.getData(this.props.endPoint, formData, this.props.method);

	    if (data.error){
		this.setState({success: false});
		return
	    }

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
