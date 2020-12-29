( function( document, jquery, constants ) {
    document.addEventListener( 'DOMContentLoaded', function() {

        /* Publisher settings
            Show/Hide publisher settings on click to dropdown
        */
        var publisherSettingsElement = document.getElementById( constants.PUBLISHER_SETTINGS_ID );
        var dropdownPublisherSettingsElement = document.getElementById( constants.DROPDOWN_PUBLISHER_ID );

        dropdownPublisherSettingsElement.addEventListener( 'click', function( e ) {
            e.preventDefault();

            var dropdownCaretElement = this.children[1];

            var isHidden = publisherSettingsElement.style.display === 'none' ? true : false;
            
            if ( isHidden ) { 
                publisherSettingsElement.style.display = 'grid'; 
                dropdownCaretElement.style.transform = 'rotate(180deg)';
            } else { 
                publisherSettingsElement.style.display = 'none'; 
                dropdownCaretElement.style.transform = '';
            }
        } );
        
    } );
} )( document, $, {
    DROPDOWN_PUBLISHER_ID: 'dropdown-publisher',
    PUBLISHER_SETTINGS_ID: 'publisher-settings'
} );