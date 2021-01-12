import alert from '../../alert';


( function( document, $ ){
    var form = document.getElementById( 'js-share-cart' );
    
    if ( !form ) return;
    
    var modal = document.getElementById( 'js-share-cart-modal' );
    var sharedCartDetails = document.getElementById( 'js-shared-cart-details' );

    form.addEventListener( 'submit', ( e ) => {
        e.preventDefault();

        var $form = $( form );
        var $modal = $( modal );
        var $sharedCartDetails = $( sharedCartDetails );
        var $sharedCodeInput = $( sharedCartDetails.firstElementChild );
        var $sharedURLCopyBtn = $( sharedCartDetails.lastElementChild );
        
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
                
                const sharedCartEndpoint = result.data.url;
                const sharedURL = `${window.location.origin}${sharedCartEndpoint}`;
                
                $sharedCodeInput.attr( 'value', sharedURL );
                $sharedURLCopyBtn.attr( 'data-clipboard-text', sharedURL );
                
                var clipboard = new ClipboardJS( `#${$sharedURLCopyBtn.attr( 'id' )}` );

                clipboard.on( 'success', ( e ) => {
                    $sharedURLCopyBtn.html( '<i class="fas fa-check"></i>' );

                    setTimeout( () => {
                        $sharedURLCopyBtn.html( 'Kopiuj' );
                    }, 2000 );

                    e.clearSelection();
                } );
                
                $form.hide();
                $sharedCartDetails.show();
            },
            error: () => {
                $modal.hide();

                alert( 'Coś poszło nie tak. Spróbuj ponownie.', 'error' );
            }
        } );
    } );
} )( document, $ );