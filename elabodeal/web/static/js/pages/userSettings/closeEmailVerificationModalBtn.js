( function( document ){
    document.addEventListener( 'click', function( e ){
        var btn = document.getElementById( 'js-close-email-verification-modal' );

        if ( !btn ) return;

        btn.addEventListener( 'click', function( e ){
            var modal = $( '#js-email-verification-modal' );

            modal.hide();
        } );
    } )
} )( document );