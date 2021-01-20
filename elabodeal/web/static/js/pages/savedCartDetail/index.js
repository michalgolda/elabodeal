import { isExistElement } from '../../utils/exist';

import ShareCartModalUIComponent from './shareCartModal';


( function( document ){
    document.addEventListener( 'DOMContentLoaded', () => {
        isExistElement( 'p-saved-cart-detail', () => {
            new ShareCartModalUIComponent();
        } );
    } );
} )( document );