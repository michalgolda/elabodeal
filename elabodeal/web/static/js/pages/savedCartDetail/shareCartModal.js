import Alert from '../../alert';
import { ALERT_MESSAGES } from '../../constants';

import httpClient from '../../utils/httpClient';

export default class ShareCartModalUIComponent {
    constructor() {
        this.elements = this.loadElements();
        this.helpers = this.loadHelpers();
        this.handlers = this.loadHandlers();

        this.bindUIActions();
    }

    bindUIActions() {
        this.elements.showModalBtn.on( 'click', () => {
            this.elements.modal.show();
        } );

        this.elements.hideModalBtn.on( 'click', () => {
            this.elements.modal.hide();
        } );

        this.elements.form.submit( this.handlers.handleSubmitShare );
    }

    loadElements() {
        return {
            modal: $( '#js-share-cart-modal' ),
            form: $( '#js-share-cart' ),
            showModalBtn: $( '#js-show-share-cart-modal' ),
            hideModalBtn: $( '#js-hide-share-cart-modal' ),
            sharedDetails: $( '#js-shared-cart-details' )
        }
    }

    loadHelpers() {
        return {
            prepareSharedCartURL: ( endpoint ) => {
                return `${ window.location.origin }${ endpoint }`;
            }
        }
    }

    loadHandlers() {
        return {
            handleSubmitShare: ( e ) => {
                e.preventDefault();

                var actionURL = this.elements.form.attr( 'action' );
                var formData = new FormData( this.elements.form.get( 0 ) );
                var data = Object.fromEntries( formData );

                httpClient.post( actionURL, data )
                    .then( response => {
                        Alert.success( ALERT_MESSAGES.CART_SAVE_SUCCESS );

                        var url = this.helpers.prepareSharedCartURL( response.data.url );
                        var urlInput = this.elements.sharedDetails.children( 'input' );
                        var urlCopyBtn = this.elements.sharedDetails.children( 'button' );
                        var urlClipboard = new ClipboardJS( `#js-copy-shared-cart-url` );

                        urlInput.val( url );
                        urlCopyBtn.attr( 'data-clipboard-text', url );

                        urlClipboard.on( 'success', ( e ) => {
                            urlCopyBtn.html( '<i class="fas fa-check"></i>' );

                            var setUrlCopyBtnTextTimeout = setTimeout( () => {
                                urlCopyBtn.html( 'Kopiuj' );
                            }, 2000 );

                            e.clearSelection();
                        } );

                        this.elements.form.hide();
                        this.elements.sharedDetails.show();
                    } )
                .catch( error => {
                    if ( error.response )
                        Alert.error( ALERT_MESSAGES.SERVER_ERROR );
                } )
            }
        }
    }
}