import alert from '../../alert';
import { DisableEditOptionMode, ToggleEditOptionMode } from './editOptionMode';

import httpClient from '../../utils/httpClient';


export default class OptionsFormUIComponent {
    constructor() {
        this.elements = this.loadElements();
        this.helpers = this.loadHelpers();
        this.handlers = this.loadHandlers();

        this.bindUIActions();
    }

    bindUIActions() {
        for ( var btn of this.elements.acceptEditOptionButtons ) {
            btn.addEventListener( 'click', ( e ) => {
                DisableEditOptionMode( e.target, true );

                this.helpers.clearInputErrors();
            } );
        }

        for ( var btn of this.elements.cancelEditOptionButtons ) {
            btn.addEventListener( 'click', ( e ) => {
                DisableEditOptionMode( e.target );

                this.helpers.clearInputErrors();
            } );
        }

        for ( var element of this.elements.toggleEditModeElements ) {
            element.addEventListener( 'click', ( e ) => {
                ToggleEditOptionMode( e.target );

                this.helpers.clearInputErrors();
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

    loadHelpers() {
        return {
            showInputErrors: ( error ) => {
                if ( error.response ) {
                    if ( error.response.status == 400 ) {
                        var errorKeys = Object.keys(error.response.data);

                        for ( var errorKey of errorKeys ) {
                            var element = this.elements.form.find(`input[name="${errorKey}"]`);
                            
                            element.addClass( 'input-error' );                            
                        }
                    }
                }
            },
            clearInputErrors: () => {
                var errorInputs = $( '.input-error' );

                for ( var errorInput of errorInputs )
                    $( errorInput ).removeClass( 'input-error' );
            },
            updateNavigationUsername: ( username ) => {
                $( '.nav__username' ).html( username );
            }
        }
    }

    loadHandlers() {
        return {
            handleSubmitSaveSettings: ( e ) => {
                e.preventDefault();

                DisableEditOptionMode();

                var actionURL = this.elements.form.attr( 'action' );
                var formData = new FormData( this.elements.form.get( 0 ) );
                var data = Object.fromEntries( formData );

                httpClient.put( actionURL, data )
                    .then( ( response ) => {
                        this.helpers.updateNavigationUsername( data.username );

                        alert( 'Ustawienia zostały pomyślnie zapisane', 'success' );
                    } )
                    .catch( ( error ) => {
                        this.helpers.showInputErrors( error );

                        alert( 'Coś poszło nie tak. Spróbuj ponownie.', 'error' );
                    } )
            },
            handleFormKeypress: ( e ) => {
                if ( e.keyCode === 13 ) {
                    e.preventDefault();

                    DisableEditOptionMode( undefined, true );

                    this.helpers.clearInputErrors();
                }
            }
        }
    }
}