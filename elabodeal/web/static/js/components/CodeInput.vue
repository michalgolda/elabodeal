<template>
    <div class="code">
        <div class="code__group">
            <template 
                v-for="index in [0, 1, 2]" 
                v-key="index"
            >
                <input
                    class="code__input"
                    type="text" 
                    maxlength="1" 
                    :ref="setInputRef"
                    :data-id="index"
                    @keydown="handleKeydown"
                    @input="handleInput"
                    @change="handleChange"
                    @paste="handlePaste"
                />
            </template>
        </div>
        <span class="code__group-separator"></span>
        <div class="code__group">
            <template 
                v-for="index in [3, 4, 5]" 
                v-key="index"
            >
                <input
                    class="code__input" 
                    type="text" 
                    maxlength="1" 
                    :ref="setInputRef"
                    :data-id="index"
                    @keydown="handleKeydown"
                    @input="handleInput"
                    @change="handleChange"
                    @paste="handlePaste"
                />
            </template>
        </div>
    </div>
</template>
<script>
export default {
    data: function () {
        return {
            keyCodes: {
                backspace: 8,
                arrowLeft: 37,
                arrowRight: 39,
            },
            inputRefs: []
        }
    },
    beforeUpdate() {
        this.inputRefs = []
    },
    methods: {
        handleBackspaceKey: function ( currentInput, currentInputId ) {            
            if ( currentInput.value ) {
                currentInput.value = '';

                this.handleChange();

                return;
            }

            const prevInput = this.inputRefs[ currentInputId - 1 ];
            
            if ( !prevInput ) return;

            prevInput.focus();
        },
        handleArrowLeftKey: function ( currentInputId ) {
            const prevField = this.inputRefs[ currentInputId - 1 ];
            
            if ( !prevField ) return;
            
            prevField.focus(); 
        },
        handleArrowRightKey: function ( currentInputId ) {
            const nextInput = this.inputRefs[ currentInputId + 1 ];
            
            if ( !nextInput ) return;
            
            nextInput.focus();
        },
        handleKeydown: function ( e ) {
            const currentInput = e.target;
            const currentInputId = parseInt( currentInput.dataset.id );

            switch( e.keyCode ) {
                case this.keyCodes.backspace:
                    this.handleBackspaceKey(
                        currentInput,
                        currentInputId
                    );
                    break;
                case this.keyCodes.arrowLeft:
                    this.handleArrowLeftKey(
                        currentInputId
                    );
                    break;
                case this.keyCodes.arrowRight:
                    this.handleArrowRightKey(
                        currentInputId
                    );
                    break; 
            }

        },
        handleInput: function ( e ) {
            const currentInput = e.target;
            const currentInputId = parseInt( currentInput.dataset.id );

            if ( currentInput && currentInput.value ) {                
                const nextInput = this.inputRefs[ currentInputId + 1 ];
                
                if ( !nextInput ) return;

                nextInput.focus();
            }
        },
        handlePaste: function ( e ) {
            e.preventDefault();

            const pasteString = e.clipboardData.getData( 'text' ).slice( 0, 6 );
        
            for ( var i = 0; i <= 5; i++ )
                this.inputRefs[ i ].value = pasteString[ i ] || '';

            this.handleChange();
        },
        handleChange: function () {
            this.$emit( "change" );

            var value = '';
            
            for ( var i = 0; i <= 5; i++ ) {
                const input = this.inputRefs[ i ];
                
                if ( input.value === '' )
                    return;
                else value += input.value;
            }

            this.$emit( "complete", value );
        },
        setInputRef: function ( el ) {
            if ( el ) this.inputRefs.push( el );
        }

    }
}
</script>