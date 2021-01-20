import axios from 'axios';

const httpClient = axios.create( {
    xsrfCookieName: 'csrftoken',
    xsrfHeaderName: 'X-CSRFtoken'
} );

export default httpClient;