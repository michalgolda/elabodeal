import { isExistElement } from '../../utils/exist';

import CartUpdateModalUIComponent from './cartUpdateModal';

( function( document ){
    document.addEventListener( 'DOMContentLoaded', () => {
        isExistElement( 'p-product-detail', () => {
            new CartUpdateModalUIComponent();
        } );
    } );
} )( document );