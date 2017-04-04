import React, { Component, cloneElement } from 'react';
import serialize from 'form-serialize';

import CreditApi from '../utils/Request.js';

class Form extends Component {
    constructor(props){
	super(props);

	this.handleSubmit = this.handleSubmit.bind(this);
    }

    componentDidMount(){
	this.condition();
    }

    condition(){
	this.props.children.map((child) => console.log(child));
    }

    handleSubmit(event){
	event.preventDefault();

	const formData = serialize(event.target);

	const request = new CreditApi();
	const data = request.getData(this.props.endPoint, formData, this.props.method);
	//this.setState({
	    //response: data.response
	//});
	this.props.data = data.response

    }

    render(){
	return(
	    <form onSubmit={this.handleSubmit}>
		<div>
		    {this.props.children}
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
