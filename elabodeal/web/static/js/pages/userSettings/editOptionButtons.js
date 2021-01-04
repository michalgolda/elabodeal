import { EditOptionBtnListener } from './editOptionBtnListener';

( function( document ){
    document.addEventListener( 'DOMContentLoaded', function(){
        var editButtons = document.querySelectorAll( '#js-edit-option-btn' );

        if ( !editButtons ) return;

        editButtons.forEach( ( btn ) => {
            btn.addEventListener( 'click', EditOptionBtnListener );
        } );
    } );
} )( document );