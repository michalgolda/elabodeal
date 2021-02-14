import apiClient from "../api";
import Alert from "../alert";


function updateSettings( 
		actionUrl, 
		data, 
		handlers = {
			errorHandler: () => null
		} 
	) {
	return apiClient.put( actionUrl, data )
		.then( response => {
			Alert.success( "Ustawienia zostały poprawnie zapisane." );
		} )
		.catch( error => {
			if ( error.response ) {
				switch ( error.response.status ) {
					case 400:
						Alert.info( "Wprowadzone dane są nieprawidłowe. Spórbuj ponwonie." )

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

const userService = {
	updateSettings
}

export default userService;