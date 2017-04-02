import React from 'react';
import render from 'react-dom';
import {
    BrowserRouter as Router,
    Switch,
    Route,
} from 'react-router-dom';

import Login from './Login.jsx';
import Solicitud from './Solicitud.jsx';


const Routing = () => (
	<Router basename="/creditcard">
	    <Switch>
		<Route exact path="/" component={Login}/>
		<Route path="/solicitud" component={Solicitud}/>
	    </Switch>
	</Router>
)

export default Routing;
