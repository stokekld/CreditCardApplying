import React, { Component } from 'react';

import Input from '../components/Input.jsx';
import Form from '../components/Form.jsx';

class Login extends Component {
    render(){
	return (
		<Form>
		    <Input
			placeholder="username"
			type='text'
			className='form-control'
			id='exampleInputEmail1'
			name="username"
			validation='isAlpha,isEmpty'
		    />
		    <Input
			placeholder="username"
			type='text'
			className='form-control'
			id='exampleInputEmail1'
			name="username"
			validation='isAlpha,isEmpty'
		    />
	    </Form>
	);
    }
}

export default Login;
