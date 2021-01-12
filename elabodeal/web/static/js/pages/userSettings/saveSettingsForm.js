import alert from '../../alert';
import { DisableEditOptionMode } from './editOptionMode';


( function( document, $ ){
    document.addEventListener( 'DOMContentLoaded', () => {
        var form = document.getElementById( 'js-settings-form' );

        if ( !form ) return;

        var $form = $( form );
    
        form.addEventListener( 'keypress', ( e ) => {
            if ( e.keyCode === 13 ) {
                e.preventDefault();

                DisableEditOptionMode( undefined, true );
            }
        } );

        form.addEventListener( 'submit', ( e ) => {
            e.preventDefault();

            DisableEditOptionMode();

            var actionURL = $form.attr( 'action' );
            var csrfToken = $( 'meta[name="csrf_token"]' ).attr( 'content' );
            var formData = $form.serializeArray();

            $.ajax( {
                url: actionURL,
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken
                },
                data: formData,
                success: () => alert( 'Ustawienia zostały pomyślnie zapisane', 'success' ),
                error: () => alert( 'Coś poszło nie tak. Spróbuj ponownie.', 'error' )
            } )
        } );
    } );
} )( document, $ );