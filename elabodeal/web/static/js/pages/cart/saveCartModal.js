import alert from '../../alert';

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

    loadConstants() {
        return {
            csrfToken: $( 'meta[name="csrf_token"]' ).attr( 'content' )
        }
    }

    loadHandlers() {
        return {
            handleSubmitSaveCart: ( e ) => {
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
                    success: () => {
                        alert( 'Koszyk został pomyślnie zapisany', 'success' );

                        this.elements.modal.hide();
                    },
                    error: () => {
                        alert( 'Coś poszło nie tak. Spróbuj ponownie', 'error' );
                    }
                } )
            }
        }
    }
}