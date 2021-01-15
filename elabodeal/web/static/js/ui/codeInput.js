export default class CodeInputUIComponent {
    constructor() {
        this.elements = this.loadElements();
        this.constants = this.loadConstants();
        this.helpers = this.loadHelpers();
        this.handlers = this.loadHandlers();

        this.bindUIActions();
    }

    bindUIActions() {
        for ( var input of this.elements.inputs ) {
            input.addEventListener( 'input', this.handlers.handleInput, false );
            input.addEventListener( 'paste', this.handlers.handlePaste, false );
            input.addEventListener( 'keydown', this.handlers.handleKeydown, false );
            input.addEventListener( 'focus', this.helpers.clearCodeInputElementsError, false );
        }
    }

    loadElements() {
        return {
            inputs: $( '.code__input' )
        }
    }

    loadHelpers() {
        return {
            getCurrentInputId: ( input ) => Number( $( input ).attr( 'aria-label' ) ),
            focusNextInput: ( input ) => {
                var nextInputId = this.helpers.getCurrentInputId( input ) + 1;

                $( this.elements.inputs[ nextInputId ] ).focus()
            },
            focusPreviousInput: ( input ) => {
                var previousInputId = this.helpers.getCurrentInputId( input ) - 1;

                $( this.elements.inputs[ previousInputId ] ).focus()
            },
            clearCodeInputElementsError: () => {
                for ( var element of this.elements.inputs )
                    element.classList.remove( 'code__input-error' );
            }
        }
    }

    loadConstants() {
        return {
            keys: {
                backspace: 8,
                arrowLeft: 37,
                arrowRight: 39
            }
        }
    }

    loadHandlers() {
        return {
            handleArrowLeft: ( e ) => {
                var input = e.target;
                
                if ( !input ) return;

                this.helpers.focusPreviousInput( input );
            },
            handleArrowRight: ( e ) => {
                var input = e.target;

                if ( !input ) return;

                this.helpers.focusNextInput( input );
            },
            handleBackspace: ( e ) => {
                var input = e.target;

                if ( input.value ) {
                    input.value = '';
                    return;
                }

                this.helpers.focusPreviousInput( input );
            },
            handleKeydown: ( e ) => {
                switch ( e.keyCode ) {
                    case this.constants.keys.backspace:
                        this.handlers.handleBackspace( e );
                        break;
                    case this.constants.keys.arrowLeft:
                        this.handlers.handleArrowLeft( e );
                        break;
                    case this.constants.keys.arrowRight:
                        this.handlers.handleArrowRight( e );
                        break;
                }
            },
            handlePaste: ( e ) => {
                e.preventDefault();
            
                const pasteData = e.clipboardData.getData( 'text' ).slice(0, 6);

                for ( var i = 0; i <= 5; i++ )
                    this.elements.inputs[ i ].value =  pasteData[ i ] || '';
            },
            handleInput: ( e ) => {
                var input = e.target;

                if ( input && input.value ) {
                    this.helpers.focusNextInput( input );
                }
            }
        }
    }
}