import React, { Component } from 'react';
import Form from '../components/Form.jsx';
import Input from '../components/Input.jsx';
import Select from '../components/Select.jsx';

class Solicitud extends Component {
    render(){
	return (
	    <Form>
		<div className="row">
		    <div className="col-md-3">
			<Input placeholder="Folio" type='text' name="folio" validation='isEmpty,isAlphanumeric' maxLength="30"/>
		    </div>
		    <div className="col-md-3">
			<Select endPoint='producto/' fieldName='producto' />
		    </div>
		</div>
		<div className="row">
		    <div className="col-md-4">
			<Input placeholder="Nombre" type='text' name="nombre" validation='isEmpty,isAlpha' maxLength="30"/>
		    </div>
		    <div className="col-md-4">
			<Input placeholder="A. Paterno" type='text' name="apellidoP" validation='isEmpty,isAlpha' maxLength="30"/>
		    </div>
		    <div className="col-md-4">
			<Input placeholder="A. Materno" type='text' name="apellidoM" validation='isEmpty,isAlpha' maxLength="30"/>
		    </div>
		</div>
		<div className="row">
		    <div className="col-md-2">
			<Input placeholder="Lada" type='text' name="lada" validation='isNumeric' maxLength="10"/>
		    </div>
		    <div className="col-md-4">
			<Input placeholder="Telefono" type='text' name="telefono" validation='isNumeric' maxLength="20"/>
		    </div>
		    <div className="col-md-6">
			<Input placeholder="E-mail" type='text' name="email" validation='isEmail' maxLength="50"/>
		    </div>
		</div>
		<hr />
		<div className="row">
		    <div className="col-md-2">
			<Select endPoint='universidad/' fieldName='universidad' />
		    </div>
		</div>
		<button type="submit" className="btn btn-default">Submit</button>
	    </Form>
	);
    }
}

export default Solicitud;
