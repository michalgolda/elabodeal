import { SaveSettingsListener } from './saveSettingsListener';


( function( document ){
    document.addEventListener( 'DOMContentLoaded', function(){
        var form = document.querySelector( '#js-settings-form' );

        if ( !form ) return;

        form.addEventListener( 'submit', SaveSettingsListener );
    } );
} )( document );