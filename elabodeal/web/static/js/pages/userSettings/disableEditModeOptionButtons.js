import { DisableEditOptionMode } from './editOptionMode';


( function( document ){
    document.addEventListener( 'DOMContentLoaded', function(){
        var disableEditModeButtons = document.querySelectorAll( '#js-cancel-edit-option-btn' );

        if ( !disableEditModeButtons ) return;

        disableEditModeButtons.forEach( ( btn ) => {
            btn.addEventListener( 'click', ( e ) => {
                DisableEditOptionMode( e.target );
            } );
        } );
    } );
} )( document );