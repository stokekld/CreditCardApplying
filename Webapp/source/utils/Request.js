import fetch from 'isomorphic-fetch';
import ToastMsg from './Toast.js';

class CreditApi{

    constructor(){
	this.baseUrl = 'http://localhost:8000/';
	this.toast = new ToastMsg();
    }

    async getData(resource, body, method='GET'){

	const data = {
	    status: 0,
	    error: false
	};

	await fetch(`${this.baseUrl}${resource}`, {
	    mode: 'cors',
	    method: method,
	    headers: {
		'X-Requested-With': "XMLHttpRequest",
		'Content-Type': "application/json"
	    },
	    body: JSON.stringify(body)
	})
	.then((response) => {
	    data.status = response.status;
	    return response.json();
	})
	.then((body) => {
	    data.response = body;
	})
	.catch((error) => {
	    data.error = true;
	    data.errorBody = error;
	    this.toast.showToast('Servicio no disponible');
	});

	return data;

    }
}

export default CreditApi;
