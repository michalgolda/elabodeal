import axios from 'axios';


const apiClient = axios.create( {
    xsrfCookieName: 'csrftoken',
    xsrfHeaderName: 'X-CSRFtoken'
} );

export default apiClient;