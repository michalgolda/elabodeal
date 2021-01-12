( function( document, $ ){
    document.addEventListener( 'DOMContentLoaded', () => {
        var btn = document.getElementById( 'js-hide-save-cart-modal' );
        var modal = document.getElementById( 'js-save-cart-modal' );

        if ( !btn || !modal ) return;

        var $modal = $( modal );

        btn.addEventListener( 'click', () => {
            $modal.hide();
        } );
    } );
} )( document, $ );