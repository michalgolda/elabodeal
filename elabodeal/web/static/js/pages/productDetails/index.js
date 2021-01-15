import CartUpdateModalUIComponent from './cartUpdateModal';

( function( document ){
    document.addEventListener( 'DOMContentLoaded', () => {
        $( 'p-product-detail' ).ready( () => {
            new CartUpdateModalUIComponent();
        } );
    } );
} )( document );