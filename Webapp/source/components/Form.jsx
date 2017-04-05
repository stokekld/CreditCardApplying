import React, { Component, cloneElement } from 'react';
import serialize from 'form-serialize';

import CreditApi from '../utils/Request.js';
import Input from './Input.jsx';

class Form extends Component {
    constructor(props){
	super(props);

	this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleSubmit(event){
	event.preventDefault();

	const arreglo = [];

	for (const key in this.refs)
	    arreglo.push(this.refs[key].state.validation);

	const validation = !arreglo.includes(false);
	
	if (validation){
	    const formData = serialize(event.target);

	    const request = new CreditApi();
	    const data = request.getData(this.props.endPoint, formData, this.props.method);

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
		//{ this.props.children.map(( child, index ) => (
		    //<div key={index}>
			//{ this.setProps(child) }
		    //</div>
		//)) }
