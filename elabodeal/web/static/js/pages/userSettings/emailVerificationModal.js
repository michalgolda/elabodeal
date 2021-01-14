import alert from '../../alert';
import { setCodeInputValue } from '../../utils/setCodeInputValue';


export default class EmailVerificationModalUIComponent {
    constructor() {
        this.elements = this.loadElements();
        this.constants = this.loadConstants();
        this.helpers = this.loadHelpers();
        this.handlers = this.loadHandlers();
        this.constants = this.loadConstants();

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

    loadConstants() {
        return {
            csrfToken: $( 'meta[name="csrf_token"]' ).attr( 'content' )
        }
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
                    element.classList.add( 'code__input-error' );
            }
        }
    }

    loadHandlers() {
        return {
            handleShowModal: () => this.elements.modal.show(),
            handleHideModal: () => this.elements.modal.hide(),
            handleSubmitVerification: ( e ) => {
                e.preventDefault();

                setCodeInputValue( e.target );

                var formData = this.elements.form.serializeArray();

                if ( formData[ 1 ].value === '' || formData[ 1 ].value.length < 6 ) return;

                var actionURL = this.elements.form.attr( 'action' );

                $.ajax( {
                    url: actionURL,
                    method: 'POST',
                    headers: {
                        'X-CSRFtoken': this.constants.csrfToken
                    },
                    data: formData,
                    success: () => {
                        alert( 'Weryfikacja powiodła się', 'success' );

                        window.location.reload();

                        this.elements.modal.hide();
                    },
                    error: () => {
                        alert( 'Coś poszło nie tak. Spróbuj ponownie.', 'error' );

                        this.helpers.showCodeInputElementsError();
                    }
                } );
            },
            handleResendCode: ( e ) => {
                var formData = this.elements.form.serializeArray();
                var actionURL = this.elements.resendCodeBtn.attr( 'data-action-url' );
                
                $.ajax( {
                    url: actionURL,
                    method: 'POST',
                    headers: {
                        'X-CSRFtoken': this.constants.csrfToken
                    },
                    data: formData,
                    success: () => {
                        alert( 'Nowy kod został wysłany', 'success' );
                        
                        this.helpers.disableResendCodeBtn();
                    },
                    error: () => {
                        alert( 'Coś poszło nie tak. Spróbuj ponownie.', 'error' );
                    }
                } );
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
            codeInputElements: $( '.code__input' )
        }
    }
}