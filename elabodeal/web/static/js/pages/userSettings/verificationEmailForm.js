import { EmailVerificationListener } from './emailVerificationListener';


( function( document ){
    document.addEventListener( 'DOMContentLoaded', function(){
        var form = document.getElementById( 'js-email-verification' );

        if ( !form ) return;

        form.addEventListener( 'submit', EmailVerificationListener );
    } );
} )( document );