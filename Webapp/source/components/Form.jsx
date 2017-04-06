import React, { Component } from 'react';
import serialize from 'form-serialize';

import CreditApi from '../utils/Request.js';
import Input from './Input.jsx';
import ToastMsg from '../utils/Toast.js';


class Form extends Component {
    constructor(props){
	super(props);

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
	    const formData = serialize(event.target);

	    const request = new CreditApi();
	    const data = await request.getData(this.props.endPoint, formData, this.props.method);


	}

    }

    render(){

	const hijos = this.props.children.map((child, index) => {
	    if (child.type === Input)
		return (
		    <Input {...child.props} key={index} ref={child.props.id}/>
		);

	    return child;
	});

	return(
	    <form onSubmit={this.handleSubmit}>
		<div>
		    {hijos}
		</div>
		<button type="submit" className="btn btn-default">Submit</button>
	    </form>
	);
    }

}

export default Form;
