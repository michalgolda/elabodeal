( function( document ){
    document.addEventListener( 'click', function(){
        var closeButtons = document.querySelectorAll( '#js-close-cart-update-modal' );
        
        if ( !closeButtons ) return;

        var modal = $( '#js-cart-update-modal' );

        closeButtons.forEach( ( btn ) => {
            btn.addEventListener( 'click', function(){
                modal.remove();
            } );
        } );
    } );
} )( document );