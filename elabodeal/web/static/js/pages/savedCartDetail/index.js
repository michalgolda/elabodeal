import isExistElement from '../../utils/isExistElement';

import ShareCartModalUIComponent from './shareCartModal';


( function( document ){
    document.addEventListener( 'DOMContentLoaded', () => {
        isExistElement( 'p-saved-cart-detail', () => {
            new ShareCartModalUIComponent();
        } );
    } );
} )( document );