import OptionsFormUIComponent from './optionsForm';
import EmailVerificationModalUIComponent from './emailVerificationModal';

( function( document ){
    document.addEventListener( 'DOMContentLoaded', () => {
        new OptionsFormUIComponent();
        new EmailVerificationModalUIComponent();
    } );
} )( document );