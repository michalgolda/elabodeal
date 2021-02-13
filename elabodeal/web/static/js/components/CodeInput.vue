<template>
    <div class="code">
        <div class="code__group">
            <template v-for="index in [0, 1, 2]">
                <input
                    :key="index"
                    :data-id="index"
                    v-on:keydown="handleKeydown"
                    v-on:input="handleInput"
                    v-on:change="handleChange"
                    v-on:paste.prevent="handlePaste"
                    ref="fields"
                    class="code__input"
                    type="text" 
                    maxlength="1" 
                />
            </template>
        </div>
        <span class="code__group-separator"></span>
        <div class="code__group">
            <template v-for="index in [3, 4, 5]">
                <input
                    :key="index"
                    :data-id="index"
                    v-on:keydown="handleKeydown"
                    v-on:input="handleInput"
                    v-on:change="handleChange"
                    v-on:paste.prevent="handlePaste"
                    ref="fields"
                    class="code__input" 
                    type="text" 
                    maxlength="1" 
                />
            </template>
        </div>
    </div>
</template>
<script>
const KEYCODES = {
    backspace: 8,
    arrowLeft: 37,
    arrowRight: 39,
}

export default {
    name: 'CodeInput',
    methods: {
        handleBackspaceKey( currentField, currentFieldId ) {            
            if ( currentField.value ) {
                currentField.value = '';

                this.handleChange();

                return;
            }

            var prevField = this.$refs.fields[ currentFieldId - 1 ];
            
            if ( !prevField ) return;

            prevField.focus();
            
        },
        handleArrowLeftKey( currentFieldId ) {
            var prevField = this.$refs.fields[ currentFieldId - 1 ];
            
            if ( !prevField ) return;
            
            prevField.focus(); 
        },
        handleArrowRightKey( currentFieldId ) {
            var nextField = this.$refs.fields[ currentFieldId + 1 ];
            
            if ( !nextField ) return;
            
            nextField.focus();
        },
        handleKeydown( e ) {
            var currentField = e.target;
            var currentFieldId = parseInt(currentField.dataset.id);

            switch( e.keyCode ) {
                case KEYCODES.backspace:
                    this.handleBackspaceKey(
                        currentField,
                        currentFieldId
                    );
                    break;
                case KEYCODES.arrowLeft:
                    this.handleArrowLeftKey(
                        currentFieldId
                    );
                    break;
                case KEYCODES.arrowRight:
                    this.handleArrowRightKey(
                        currentFieldId
                    );
                    break; 
            }

        },
        handleInput( e ) {
            var currentField = e.target;
            var currentFieldId = parseInt(currentField.dataset.id);

            if ( currentField && currentField.value ) {                
                var nextField = this.$refs.fields[ currentFieldId + 1 ];
                
                if ( !nextField ) return;

                nextField.focus();
            }
        },
        handlePaste( e ) {
            var pasteString = e.clipboardData.getData( 'text' ).slice( 0, 6 );
        
            for ( var i = 0; i <= 5; i++ )
                this.$refs.fields[ i ].value = pasteString[ i ] || '';

            this.handleChange();
        },
        handleChange() {
            this.$emit( "change" );

            var value = '';
            
            for ( var i = 0; i <= 5; i++ ) {
                var field = this.$refs.fields[ i ];
                
                if ( field.value === '' )
                    return;
                else value += field.value;
            }

            this.$emit( "complete", value );
        }

    }
}
</script>