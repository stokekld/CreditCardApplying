import React, { Component } from 'react';

class Toast extends Component {
    constructor(props){
	super(props);
    }

    render(){
	return (
	    <div className="snackbar show">{this.props.message}</div>
	);
    }

}

export default Toast;
