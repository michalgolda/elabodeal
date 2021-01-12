import alert from '../../alert';


( function( document, $ ){
    document.addEventListener( 'DOMContentLoaded', () => {
        var form = document.getElementById( 'js-save-cart' );
        var modal = document.getElementById( 'js-save-cart-modal' );

        if ( !form || !modal ) return

        form.addEventListener( 'submit', ( e ) => {
            e.preventDefault();
        
            var $form = $( e.target );
            var $modal = $( modal );

            const actionURL = $form.attr( 'action' );
            const csrfToken = $( 'meta[name="csrf_token"]' ).attr( 'content' );
            const formData = $form.serializeArray();
            
            $.ajax( {
                url: actionURL,
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken
                },
                data: formData,
                success: ( result ) => {
                    $modal.hide();

                    alert( 'Koszyk zostł pomyślnie zapisany', 'success' );
                },
                error: ( error ) => {
                    $modal.hide();

                    alert( 'Coś poszło nie tak. Spróbuj ponownie.', 'error' );
                }
            } );
        } );
    } );
} )( document, $ );