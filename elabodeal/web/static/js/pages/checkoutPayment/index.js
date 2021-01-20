import { isExistElement } from '../../utils/exist';

import PaymentFormUIComponent from './paymentForm';


( function( document ){
    document.addEventListener( 'DOMContentLoaded', () => {
        isExistElement( 'p-cart-checkout-payment', () => {
            new PaymentFormUIComponent();
        } );
    } );
} )( document );