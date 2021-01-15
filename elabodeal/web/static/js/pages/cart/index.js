import SaveCartModalUIComponent from './saveCartModal';

( function( document ){
    document.addEventListener( 'DOMContentLoaded', () => {
        $( 'p-cart' ).ready( () => {
            new SaveCartModalUIComponent();
        } );
    } );
} )( document );