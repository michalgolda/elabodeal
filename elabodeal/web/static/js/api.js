import axios from 'axios';


const apiClient = axios.create( {
    xsrfCookieName: 'csrftoken',
    xsrfHeaderName: 'X-CSRFtoken',
    headers: {
    	'content-type': 'multipart/form-data'
    }
} );

export default apiClient;