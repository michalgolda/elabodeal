import ScrollUpBtnUIComponent from './scrollupBtn';
import NavigationUIComponent from './navigation';

( function( document ){
    document.addEventListener( 'DOMContentLoaded', () => {
        new NavigationUIComponent();
        new ScrollUpBtnUIComponent();
    } );
} )( document );