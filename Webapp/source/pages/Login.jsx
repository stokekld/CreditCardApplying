import React, { Component } from 'react';

import Input from '../components/Input.jsx';
import Form from '../components/Form.jsx';
import ToastMsg from '../utils/Toast.js';


class Login extends Component {
    constructor(props){
	super(props);
    }

    triggerSubmit(response, status, toast){
	if (status == 404)
	    toast.showToast('No se ha encontrado el usuario');
	else if (status == 200){
	    toast.showToast('Bienvenido');
	    window.sessionStorage.removeItem('token');
	    window.sessionStorage.setItem('token', response.data.token);
	    setTimeout(() => window.location.replace('solicitud'), 3000);
	}

    }

    render(){
	return (
	    <div className="row">
		<div className="col-md-4 col-md-offset-4">
		    <Form endPoint="usuarios/auth/" method="POST" trigger={this.triggerSubmit}>
			<Input placeholder="Usuario" type='text' name="user" validation='isEmpty,isAlpha' />
			<Input placeholder="Password" type='password' name="password" validation='isEmpty' />
			<button type="submit" className="btn btn-default">Submit</button>
		    </Form>
		</div>
	    </div>
	);
    }
}

export default Login;
