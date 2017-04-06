import React from 'react';
import { render, unmountComponentAtNode } from 'react-dom';

import Toast from '../components/Toast.jsx';

class ToastMsg{
    constructor(){
	this.id = 'toast';
    }

    showToast(message){
	render(<Toast message={message}/>, document.getElementById(this.id));

	setTimeout(() => this.hideToast(), 3000);
    }
    
    hideToast(){
	unmountComponentAtNode(document.getElementById(this.id));
    }
}

export default ToastMsg;
