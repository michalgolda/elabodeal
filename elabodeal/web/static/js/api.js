import axios from 'axios';
import Alert from '@/alert';


const apiClient = axios.create({
    xsrfCookieName: 'csrftoken',
    xsrfHeaderName: 'X-CSRFtoken',
    headers: {
    	'content-type': 'multipart/form-data'
    }
});

apiClient.interceptors.response.use(
    function (res) { return res },
    function (err) {
        const errResponse = err.response;

        if (errResponse) {
            const errResponseStatus = errResponse.status;

            const isUnexpectedErr = errResponseStatus === 500;

            if (isUnexpectedErr)
                Alert.error( 
                    `Wystąpił niespowdziewany błąd.
                    Po zlokalizowaniu usterki, 
                    postaramy się ją jak najszybciej usunąć.` 
                );

            return Promise.reject(errResponse);
        }
    }
);

export default apiClient;