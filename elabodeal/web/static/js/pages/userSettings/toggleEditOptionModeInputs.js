import { ToggleEditOptionMode } from './editOptionMode';


( function( document ){
    document.addEventListener( 'DOMContentLoaded', function(){
        var toggleEditModeInputs = document.querySelectorAll( '#js-option-input' );

        if ( !toggleEditModeInputs ) return;

        toggleEditModeInputs.forEach( ( input ) => {
            input.addEventListener( 'click', ( e ) => {
                ToggleEditOptionMode( e.target );
            } );
        } );
    } );
} )( document );