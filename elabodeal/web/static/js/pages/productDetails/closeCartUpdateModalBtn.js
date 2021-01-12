( function( document ){
    document.addEventListener( 'click', () => {
        var closeButtons = document.querySelectorAll( '#js-hide-cart-update-modal' );
        var modal = document.getElementById( 'js-cart-update-modal' );

        if ( !closeButtons || !modal ) return;

        var $modal = $( modal );

        closeButtons.forEach( ( btn ) => {
            btn.addEventListener( 'click', () => {
                $modal.remove();
            } );
        } );
    } );
} )( document );