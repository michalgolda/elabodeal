( function( document, $ ){
    document.addEventListener( 'DOMContentLoaded', () => {
        var btn = document.getElementById( 'js-hide-share-cart-modal' );
        var modal = document.getElementById( 'js-share-cart-modal' );

        if ( !btn || !modal ) return;

        var $modal = $( modal );

        btn.addEventListener( 'click', () => {
            $modal.hide();
        } );
    } );
} )( document, $ )