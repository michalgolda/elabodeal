( function( document ){
    document.addEventListener( 'click', () => {
        var btn = document.getElementById( 'js-hide-email-verification-modal' );
        var modal = document.getElementById( 'js-email-verification-modal' );

        if ( !btn || !modal ) return;
        
        var $modal = $( modal );

        btn.addEventListener( 'click', () => {
            $modal.hide();
        } );
    } )
} )( document );