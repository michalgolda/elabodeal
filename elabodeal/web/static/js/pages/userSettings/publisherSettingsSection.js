import { SectionDropdown } from './sectionDropdown';

( function( document ){
    document.addEventListener( 'DOMContentLoaded', function(){
        var trigger = document.querySelector( '#js-trigger-publisher-settings-section' );
        var section = document.querySelector( '#js-publisher-settings-section' );

        if ( !trigger || !section ) return;

        SectionDropdown(trigger, section);
    } );
} )( document );