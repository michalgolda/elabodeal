( function( document ){
    document.addEventListener( 'DOMContentLoaded', function(){
        var startEmailVerificationBtn = document.getElementById( 'js-start-email-verification-btn' );
        
        if ( !startEmailVerificationBtn ) return;

        startEmailVerificationBtn.addEventListener( 'click', function( e ){
            e.preventDefault();
            
            var modal = $( '#js-email-verification-modal' );

            modal.show();
        } );
    } );
} )( document );