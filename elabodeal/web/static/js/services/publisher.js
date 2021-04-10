import apiClient from "../api";
import Alert from "../alert";


function createProduct(
		actionURL,
		data,
		successHandler = () => null,
		errorHandler = () => null
	) {
	return apiClient.post( actionURL, data )
		.then( response => {
			Alert.success( "Produkt został pomyślnie dodany." );
		
			successHandler( response );
		} )
		.catch( error => {
			if ( error.response ) {
				switch ( error.response.status ) {
					case 400:
						Alert.info( "Popraw błędy w formularzu." );

						errorHandler( error );

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

const publisherService = {
	createProduct
}

export default publisherService;