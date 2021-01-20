import alert from '../../../alert';
import { setCodeInputValue } from '../../../utils/setCodeInputValue';

import httpClient from '../../../utils/httpClient';

export default class EmailVerificationModalUIComponent {
    constructor() {
        this.elements = this.loadElements();
        this.helpers = this.loadHelpers();
        this.handlers = this.loadHandlers();

        this.bindUIActions();
    }

    bindUIActions() {
        this.elements.showModalBtn.on( 
            'click', 
            this.handlers.handleShowModal
        );

        this.elements.hideModalBtn.on(
            'click',
            this.handlers.handleHideModal
        );
        
        this.elements.form.submit( this.handlers.handleSubmitVerification );

        this.elements.resendCodeBtn.on( 
            'click',
            this.handlers.handleResendCode
        );
    }

    loadHelpers() {
        return {
            disableResendCodeBtn: () => {
                var seconds = 59;

                var timerInterval = setInterval( () => {
                    this.elements.resendCodeBtn.html( `Spróbuj ponownie za ${ seconds }`);
                    this.elements.resendCodeBtn.addClass( 'btn-disabled' );
                    this.elements.resendCodeBtn.attr( 'disabled', 'disabled' );
                    this.elements.resendCodeBtn.removeClass( 'btn__secondary-outline' );

                    seconds--;
                }, 1000 );

                var timerTimeout = setTimeout( () => {
                    clearInterval( timerInterval );

                    this.elements.resendCodeBtn.html( 'Wyślij kod ponownie' );
                    this.elements.resendCodeBtn.removeClass( 'btn-disabled' );
                    this.elements.resendCodeBtn.removeAttr( 'disabled' );
                    this.elements.resendCodeBtn.addClass( 'btn__secondary-outline' ); 
                }, 60000 );
            },
            showCodeInputElementsError: () => {
                for ( var element of this.elements.codeInputElements )
                    element.classList.add( 'input-error' );
            }
        }
    }

    loadHandlers() {
        return {
            handleShowModal: () => {
                var actionURL = this.elements.resendCodeBtn.attr( 'data-action-url' );
                var formData = new FormData( this.elements.form.get( 0 ) );
                var data = Object.fromEntries( formData );

                httpClient.post( actionURL, data );

                this.elements.modal.show();
            },
            handleHideModal: () => this.elements.modal.hide(),
            handleSubmitVerification: ( e ) => {
                e.preventDefault();

                setCodeInputValue( e.target );

                var actionURL = this.elements.form.attr( 'action' );
                var formData = new FormData( this.elements.form.get( 0 ) );
                var data = Object.fromEntries( formData );

                if ( data[ 'code' ].length < 6 || data[ 'code' ].length > 6)
                    return;

                httpClient.post( actionURL, data )
                    .then( response => {
                        alert( 'Weryfikacja powiodła się', 'success' );
                        
                        this.elements.modal.remove();
                        this.elements.infoAboutEmailVerification.remove();

                        window.location.reload();
                    } )
                    .catch( error => {
                        alert( 'Coś poszło nie tak. Spróbuj ponownie.', 'error' );
                        
                        this.helpers.showCodeInputElementsError();
                    } )
            },
            handleResendCode: ( e ) => {
                var actionURL = this.elements.resendCodeBtn.attr( 'data-action-url' );
                var formData = new FormData( this.elements.form.get( 0 ) );
                var data = Object.fromEntries( formData );

                httpClient.post( actionURL, data )
                    .then( response => {
                        alert( 'Nowy kod został wysłany', 'success' );
                        
                        this.helpers.disableResendCodeBtn();
                    } )
                    .catch( error => {
                        alert( 'Coś poszło nie tak. Spróbuj ponownie.', 'error' );
                    } )
            }
        }
    }

    loadElements() {
        return {
            form: $( '#js-email-verification' ),
            modal: $( '#js-email-verification-modal' ),
            showModalBtn: $( '#js-show-email-verification-modal' ),
            hideModalBtn: $( '#js-hide-email-verification-modal' ),
            resendCodeBtn: $( '#js-resend-email-verification-code' ),
            codeInputElements: $( '.code__input' ),
            infoAboutEmailVerification: $( '#js-show-email-verification-modal' ).parent( 'div' )
        }
    }
}