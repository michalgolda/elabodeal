import axios from 'axios';


export const SaveSettingsListener = ( e ) => {
    e.preventDefault();

    var form = $( e.target );
    var submitBtn = $( e.submitter );
    
    var actionURL = form.attr( 'action' );

    // Clear current editing option
    const currentEditing = window.currentEditing;
    if ( currentEditing )
        currentEditing.forEach( ( element ) => {
            switch( element.id ) {
                case 'js-edit-option-btn':
                    element.style.display = 'block';
                    break;
                case 'js-cancel-edit-option-btn':
                    element.style.display = 'none';
                    break;
                case 'js-option-input':
                    element.classList.remove( 'current-editing-input' );
                    break;
            }
        } );
        
        delete window.currentEditing;
    
    var formData = new FormData( form.get( 0 ) );
        
    axios.post( actionURL, formData, {
        headers: {
            'X-CSRFtoken': window.__csrf_token__
        }
    })
        .catch( ( error ) => {
            console.error(error);
        } )
};