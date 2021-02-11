import EmailVerificationModalUIComponent from './emailVerificationModal';

import { isExistElement } from '../../../utils/exist';


( function( window ){
    window.addEventListener( 'DOMContentLoaded', () => {
        isExistElement( 'p-user-settings', () => {        
            new EmailVerificationModalUIComponent();
        } );
    } );
} )( window );