import { DisableEditOptionMode } from './editOptionMode';


( function( document, $ ){
    document.addEventListener( 'DOMContentLoaded', () => {
        var acceptEditButtons = document.querySelectorAll( '#js-accept-edit-option-btn' );

        if ( !acceptEditButtons ) return;

        acceptEditButtons.forEach( btn => {
            btn.addEventListener( 'click', ( e ) => {
                DisableEditOptionMode( e.target, true );
            } );
        } );
    } );
} )( document, $ );