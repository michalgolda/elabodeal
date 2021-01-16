import isExistElement from '../../utils/isExistElement';

import SaveCartModalUIComponent from './saveCartModal';


( function( document ){
    document.addEventListener( 'DOMContentLoaded', () => {
        isExistElement( 'p-cart', () => {
            new SaveCartModalUIComponent();
        } );
    } );
} )( document );