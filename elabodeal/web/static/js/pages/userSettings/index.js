import isExistElement from '../../utils/isExistElement';

import CodeInputUIComponent from '../../ui/codeInput';

import OptionsFormUIComponent from './optionsForm';
import EmailVerificationModalUIComponent from './emailVerificationModal';


( function( document ){
    document.addEventListener( 'DOMContentLoaded', () => {
        isExistElement( 'p-user-settings', () => {
            new OptionsFormUIComponent();            
            new EmailVerificationModalUIComponent();
            new CodeInputUIComponent();
        } );
    } );
} )( document );