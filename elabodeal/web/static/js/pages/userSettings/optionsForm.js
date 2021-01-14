import alert from '../../alert';
import { DisableEditOptionMode, ToggleEditOptionMode } from './editOptionMode';


export default class OptionsFormUIComponent {
    constructor() {
        this.elements = this.loadElements();
        this.constants = this.loadConstants();
        this.handlers = this.loadHandlers();

        this.bindUIActions();
    }

    bindUIActions() {
        for ( var btn of this.elements.acceptEditOptionButtons ) {
            btn.addEventListener( 'click', ( e ) => {
                DisableEditOptionMode( e.target, true );
            } );
        }

        for ( var btn of this.elements.cancelEditOptionButtons ) {
            btn.addEventListener( 'click', ( e ) => {
                DisableEditOptionMode( e.target );
            } );
        }

        for ( var element of this.elements.toggleEditModeElements ) {
            element.addEventListener( 'click', ( e ) => {
                ToggleEditOptionMode( e.target );
            } );
        }

        this.elements.form.on( 'submit', this.handlers.handleSubmitSaveSettings );
        this.elements.form.on( 'keypress', this.handlers.handleFormKeypress );
    }

    loadElements() {
        return {
            form: $( '#js-settings-form' ),
            acceptEditOptionButtons: $( '.js-accept-edit-option' ),
            cancelEditOptionButtons: $( '.js-cancel-edit-option' ),
            toggleEditModeElements: $( '.js-edit-option' )
        }
    }

    loadConstants() {
        return {
            csrfToken: $( 'meta[name="csrf_token"]' ).attr( 'content' )
        }
    }

    loadHandlers() {
        return {
            handleSubmitSaveSettings: ( e ) => {
                e.preventDefault();

                DisableEditOptionMode();

                var actionURL = this.elements.form.attr( 'action' );
                var formData = this.elements.form.serializeArray();

                $.ajax( {
                    url: actionURL,
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': this.constants.csrfToken
                    },
                    data: formData,
                    success: () => alert( 'Ustawienia zostały pomyślnie zapisane', 'success' ),
                    error: () => alert( 'Coś poszło nie tak. Spróbuj ponownie.', 'error' )
                } )
            },
            handleFormKeypress: ( e ) => {
                if ( e.keyCode === 13 ) {
                    e.preventDefault();

                    DisableEditOptionMode( undefined, true );
                }
            }
        }
    }
}