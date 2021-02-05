import Alert from '../../alert';
import { ALERT_MESSAGES } from '../../constants';

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
        
        for ( var input of this.elements.optionInputs ) {
            input.addEventListener( 
                'change', 
                this.handlers.handleChangeOptionInput 
            );
        }

        this.elements.form.on( 'submit', this.handlers.handleSubmitSaveSettings );
        this.elements.form.on( 'keypress', this.handlers.handleFormKeypress );
    }

    loadElements() {
        return {
            form: $( '#js-settings-form' ),
            acceptEditOptionButtons: $( '.js-accept-edit-option' ),
            cancelEditOptionButtons: $( '.js-cancel-edit-option' ),
            toggleEditModeElements: $( '.js-edit-option' ),
            optionInputs: $( '.js-option-input' )
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
                    .then( response => {
                        this.helpers.updateNavigationUsername( data.username );

                        Alert.success( ALERT_MESSAGES.SETTINGS_SAVE_SUCCESS );
                    } )
                    .catch( error => {
                        if ( error.response ) {
                            switch ( error.response.status ) {
                                case 400:
                                    Alert.info( ALERT_MESSAGES.BAD_REQUEST );
                                default:
                                    Alert.error( ALERT_MESSAGES.SERVER_ERROR );
                            }
                        }
                    } )
            },
            handleFormKeypress: ( e ) => {
                if ( e.keyCode === 13 ) {
                    e.preventDefault();

                    DisableEditOptionMode( undefined, true );
                    
                    var changeEvent = new Event( 'change' );
                    e.target.dispatchEvent( changeEvent );

                    this.helpers.clearInputErrors();
                }
            },
            handleChangeOptionInput: ( e ) => {
                var targetValue = e.target.value;
                
                if ( targetValue.length === 0 )
                    DisableEditOptionMode( e.target );
            }
        }
    }
}