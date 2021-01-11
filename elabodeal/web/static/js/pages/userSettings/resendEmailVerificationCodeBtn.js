( function( document ){
    document.addEventListener( 'DOMContentLoaded', function(){
        var resendBtn = document.getElementById( 'js-resend-email-verification-code-btn' );

        if ( !resendBtn ) return;

        resendBtn.addEventListener( 'click', function( e ){
            var btn = $( e.target );
            var form = $( btn.get( 0 )[ 'form' ] );

            const formData = new FormData( form.get( 0 ) );
            const actionURL = btn.attr( 'data-action-url' );
        
            var msg = $( document.getElementById( 'js-email-verification-msg' ) );

            axios.post( actionURL, formData, {
                'headers': {
                    'X-CSRFtoken': window.__csrf_token__
                }
            } )
                .then( function(){
                    if ( msg.is( ':hidden' ) ) msg.show();

                    msg.addClass( 'success-msg' );
                    msg.html( 'Nowy kod został wysłany' );

                    var seconds = 1;
                    function disableResendTimer() {
                        btn.html( `Ponów próbę za ${seconds}s` );
                        btn.addClass( 'btn-disabled' );
                        btn.attr( 'disabled', 'disabled' );
                        btn.removeClass( 'btn__secondary-outline' );

                        seconds++;
                    }

                    var disableResendTimerInverval = setInterval(disableResendTimer, 1000);

                    setTimeout( function(){
                        clearInterval( disableResendTimerInverval );

                        btn.html( 'Wyślij kod ponownie' );
                        btn.removeClass( 'btn-disabled' );
                        btn.removeAttr( 'disabled' );
                        btn.addClass( 'btn__secondary-outline' );
                    }, 20000 );

                    setTimeout( function(){
                        msg.hide();

                        msg.removeClass( 'success-msg' );
                    }, 3000 );
                } )
                .catch( function(){
                    if ( msg.is( ':hidden' ) ) msg.show();

                    msg.addClass( 'error-msg' );
                    msg.html( 'Coś poszło nie tak. Spróbuj ponownie.' )

                    setTimeout( function(){
                        msg.hide();

                        msg.removeClass( 'error-msg' );
                    }, 3000 );
                } ) 
        } );
    } );
} )( document );