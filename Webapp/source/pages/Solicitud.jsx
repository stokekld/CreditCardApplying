import React, { Component } from 'react';
import Form from '../components/Form.jsx';
import Input from '../components/Input.jsx';

class Solicitud extends Component {
    render(){
	return (
	    <Form>
		<div className="row">
		    <div className="col-md-3">
			<Input placeholder="Folio" type='text' className='form-control' ref='folioSol' name="folio" validation='isEmpty,isAlphanumeric' maxLength="30"/>
			<button type="submit" className="btn btn-default">Submit</button>
		    </div>
		</div>
	    </Form>
	);
    }
}

export default Solicitud;
