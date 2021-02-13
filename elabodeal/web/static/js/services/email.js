import apiClient from '../api';
import Alert from '../alert';


function confirmEmail( 
        actionUrl, 
        data, 
        handlers = {
            successHandler: () => null,
            errorHandler: () => null
        }
    ) {
    return apiClient.post( actionUrl, data )
        .then( response => {
            Alert.success( 'Twój adres email został pomyślnie zweryfikowany.' );

            handlers.successHandler( response );
        } )
        .catch( error => {
            if ( error.response ) {
                switch ( error.response.status ) {
                    case 400:
                        Alert.info( 'Podany kod weryfikacyjny jest nieprawidłowy. Spróbuj ponownie.' );
                        
                        handlers.errorHandler( error );
                        
                        break;
                    default:
                        Alert.error( 
                            `Wystąpił błąd po stronie serwera. 
                            Po zlokalizowaniu usterki, 
                            postaramy się jak najszybciej ją usunąć :)` 
                        );
                }
            }
        } )
}

function resendConfirmEmail( actionUrl, data ) {
    return apiClient.post( actionUrl, data )
        .then( response => {
            Alert.success( 'Nowy kod został wygenerowany i wysłany na podany adres email.' );
        } )
        .catch( error => {
            if ( error.response ) {
                Alert.error( 
                    `Wystąpił błąd po stronie serwera. 
                    Po zlokalizowaniu usterki, 
                    postaramy się jak najszybciej ją usunąć :)` 
                );
            }
        } )
}


const emailService = {
    confirmEmail,
    resendConfirmEmail
}

export default emailService;