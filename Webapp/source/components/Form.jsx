import React, { Component, cloneElement } from 'react';

class Form extends Component {
    constructor(props){
	super(props);

	//this.handleChange = this.handleChange.bind(this);
    }

    setProps(component){

	//if ( component.type.name == "Input" )
	    //return cloneElement(component, {
		//onChange: this.handleChange,
	//})
	console.log(component);

	return component;

    }

    render(){
	return(
	    <div>
		{ this.props.children.map(( child, index ) => (
		    <div key={index}>
			{ this.setProps(child) }
		    </div>
		)) }
	    </div>
	);
    }

}

export default Form;
