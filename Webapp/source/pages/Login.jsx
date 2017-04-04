import React, { Component } from 'react';

import Input from '../components/Input.jsx';
import Form from '../components/Form.jsx';


class Login extends Component {
    constructor(props){
	super(props);

	this.state = {
	    data: {}
	};
    }

    componentDidUpdate(){
	console.log("se actualizo");
    }

    render(){
	return (
	    <div className="row">
		<div className="col-md-4 col-md-offset-4">
		    <Form endPoint="usuarios/auth/" method="POST" data={this.state.data}>
			<Input
			    placeholder="Usuario"
			    type='text'
			    className='form-control'
			    value='hola'
			    id='inputUser'
			    name="user"
			    validation='isEmpty,isAlpha'
			/>
			<Input
			    placeholder="Password"
			    type='password'
			    className='form-control'
			    value=''
			    id='inputPass'
			    name="password"
			    validation='isEmpty'
			/>
		    </Form>
		</div>
	    </div>
	);
    }
}

export default Login;
