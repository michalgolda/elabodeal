import { isExistElements } from '../../utils/exist';

import CodeInputUIComponent from '../../ui/codeInput';
import OptionsFormUIComponent from './optionsForm';


( function( document ){
    document.addEventListener( 'DOMContentLoaded', () => {
        isExistElements( 'p-settings', () => {
            new OptionsFormUIComponent();            
            new CodeInputUIComponent();
        } );
    } );
} )( document );