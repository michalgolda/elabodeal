import PaymentFormUIComponent from './paymentForm';

( function( document ){
    document.addEventListener( 'DOMContentLoaded', () => {
        $( 'p-cart-checkout-payment' ).ready( () => {
            new PaymentFormUIComponent();
        } );
    } );
} )( document );