import Alert from '../../alert';
import { ALERT_MESSAGES } from '../../constants';

import httpClient from '../../utils/httpClient';


export default class SaveCartModalUIComponent {
    constructor() {
        this.elements = this.loadElements();
        this.constants = this.loadConstants();
        this.handlers = this.loadHandlers();

        this.bindUIActions();
    }

    bindUIActions() {
        this.elements.showModalBtn.on( 
            'click', 
            () => this.elements.modal.show() 
        );

        this.elements.hideModalBtn.on( 
            'click',
            () => this.elements.modal.hide()
        );

        this.elements.form.submit( this.handlers.handleSubmitSaveCart );
    }

    loadElements() {
        return {
            modal: $( '#js-save-cart-modal' ),
            form: $( '#js-save-cart' ),
            showModalBtn: $( '#js-show-save-cart-modal' ),
            hideModalBtn: $( '#js-hide-save-cart-modal' )
        }
    }

    loadHandlers() {
        return {
            handleSubmitSaveCart: ( e ) => {
                e.preventDefault();

                var actionURL = this.elements.form.attr( 'action' );
                var formData = new FormData( this.elements.form.get( 0 ) );
                var data = Object.fromEntries( formData );

                httpClient.post( actionURL, data )
                    .then( response => {
                        Alert.success( ALERT_MESSAGES.CART_SAVE_SUCCESS );
                    } )
                    .catch( error => {
                        if ( error.response ) {
                            switch ( error.response.status ) {
                                case 400:
                                    Alert.info( ALERT_MESSAGES.BAD_REQUEST );

                                    break;
                                default:
                                    Alert.error( ALERT_MESSAGES.SERVER_ERROR );
                            }
                        }
                    } )
            }
        }
    }
}