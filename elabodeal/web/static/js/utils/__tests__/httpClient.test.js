import httpClient from '../httpClient';


describe( 'Test httpClient instance of axios object', () => {
    test( 'Test client xsrfCookieName option', () => {
        expect( 
            httpClient.defaults.xsrfCookieName
        ).toEqual( 'csrftoken' );
    } );

    test( 'Test client xsrfHeaderName option', () => {
        expect(
            httpClient.defaults.xsrfHeaderName
        ).toEqual( 'X-CSRFtoken' );
    } );
} );