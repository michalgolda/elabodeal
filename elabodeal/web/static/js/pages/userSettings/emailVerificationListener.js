export const EmailVerificationListener = ( e ) => {
    e.preventDefault();

    var form = $( e.target );
    
    const formData = new FormData( form.get( 0 ) );
    const formActionURL = form.attr( 'action' );

    var msg = $( document.getElementById( 'js-email-verification-msg' ) );
    
    // This element is showed if request status is success
    const successElement = '<p class="success-msg">Email został pomyślnie zweryfikowany <i class="fas fa-check"></i></p>'

    axios.post( formActionURL, formData, {
        'headers': {
            'X-CSRFtoken': window.__csrf_token__
        }
    } )
        .then( function(){
            form.empty();
            form.html( successElement );

            var modal = $( '#js-email-verification-modal' );

            // This variable is required for get info container which contain shwoing modal btn
            var openModalBtn = document.getElementById( 'js-start-email-verification-btn' );

            var infoContainer = $( openModalBtn.parentElement );
            
            setTimeout( function(){
                modal.remove();
                infoContainer.remove();
            }, 2000 );
        } )
        .catch( function(){
            if ( msg.is( ':hidden' ) ) msg.show();
            
            msg.show();

            msg.addClass( 'error-msg' );
            msg.html( 'Niepoprawny kod weryfikacyjny. Spróbuj ponownie.' );

            setTimeout( function(){
                msg.hide();
                msg.removeClass( 'error-msg' );
            }, 3000 );
        } )
}