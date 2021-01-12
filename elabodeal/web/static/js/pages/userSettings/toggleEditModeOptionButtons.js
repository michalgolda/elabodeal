import { ToggleEditOptionMode } from './editOptionMode';


( function( document ){
    document.addEventListener( 'DOMContentLoaded', function(){
        var toggleEditModeButtons = document.querySelectorAll( '#js-edit-option-btn' );

        if ( !toggleEditModeButtons ) return;

        toggleEditModeButtons.forEach( ( btn ) => {
            btn.addEventListener( 'click', ( e ) => {
                ToggleEditOptionMode( e.target );
            } );
        } );
    } );
} )( document );