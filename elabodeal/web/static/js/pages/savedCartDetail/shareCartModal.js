import alert from '../../alert';


export default class ShareCartModalUIComponent {
    constructor() {
        this.elements = this.loadElements();
        this.constants = this.loadConstants();
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

    loadConstants() {
        return {
            csrfToken: $( 'meta[name="csrf_token"]' ).attr( 'content' )
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

                var formData = this.elements.form.serializeArray();
                var actionURL = this.elements.form.attr( 'action' );

                $.ajax( {
                    url: actionURL,
                    method: 'POST',
                    headers: {
                        'X-CSRFtoken': this.constants.csrfToken
                    },
                    data: formData,
                    success: ( response ) => {
                        alert( 'Koszyk został pomyślnie udostępniony.', 'success' );

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
                    },
                    error: () => {
                        alert( 'Coś poszło nie tak. Spróbuj ponownie.', 'error' );
                    }
                } );
            }
        }
    }
}