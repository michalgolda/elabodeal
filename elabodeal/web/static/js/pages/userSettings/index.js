import OptionsFormUIComponent from './optionsForm';
import CodeInputUIComponent from '../../ui/codeInput';
import EmailVerificationModalUIComponent from './emailVerificationModal';

( function( document ){
    document.addEventListener( 'DOMContentLoaded', () => {
        $( 'p-user-settings' ).ready( () => {
            new OptionsFormUIComponent();
            new EmailVerificationModalUIComponent();
            new CodeInputUIComponent();
        } );
    } );
} )( document );