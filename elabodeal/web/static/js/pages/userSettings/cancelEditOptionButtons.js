import { CancelEditOptionBtnListener } from './cancelEditOptionBtnListener';

( function( document ){
    document.addEventListener( 'DOMContentLoaded', function(){
        var cancelButtons = document.querySelectorAll( '#js-cancel-edit-option-btn' );

        if ( !cancelButtons ) return;

        cancelButtons.forEach( ( btn ) => {
            btn.addEventListener( 'click', CancelEditOptionBtnListener );
        } );
    } );
} )( document );