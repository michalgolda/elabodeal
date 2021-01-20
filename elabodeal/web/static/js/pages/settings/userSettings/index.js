import EmailVerificationModalUIComponent from './emailVerificationModal';
import { isExistElement } from '../../../utils/exist';


( function( document ){
    document.addEventListener( 'DOMContentLoaded', () => {
        isExistElement( 'p-user-settings', () => {        
            new EmailVerificationModalUIComponent();
        } );
    } );
} )( document );