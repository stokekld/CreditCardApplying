import React, { Component } from 'react';
import CreditApi from '../utils/Request';

class Select extends Component {
    constructor(props){
	super(props);

	this.rest = new CreditApi();

	this.state = {
	    options: []
	};

	this.getOptions();
    }

    async getOptions(){
	const data = await this.rest.getData(this.props.endPoint);

	this.setState({
	    options: data.response.data
	});
    }

    render(){

	const fieldName = this.props.fieldName;

	return (
	    <select className="form-control">
		{ this.state.options.map(option => (
		    <option key={option.id} value={option.id}>{option[fieldName]}</option>
		)) }
	    </select>
	);

    }
}

export default Select;
