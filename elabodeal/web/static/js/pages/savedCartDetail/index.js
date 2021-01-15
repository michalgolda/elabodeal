import ShareCartModalUIComponent from './shareCartModal';


( function( document ){
    document.addEventListener( 'DOMContentLoaded', () => {
        $( 'p-saved-cart-detail' ).ready( () => {
            new ShareCartModalUIComponent();
        } );
    } );
} )( document );