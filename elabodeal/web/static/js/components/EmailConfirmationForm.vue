<template>
    <form v-on:submit.prevent="handleSubmit">
        <code-input
            v-bind:class="{ 'code-invalid': invalidCode }"
            v-on:complete="setCodeValue"
            v-on:change="handleChange"
            style="margin-top: 2rem; margin-bottom: 2rem;" 
        />
        <div class="flex-center">
            <button 
                class="btn btn__secondary"
                style="margin-left: .5rem; margin-right: .5rem;"
                type="submit"
            >
                Zweryfikuj
            </button>
            <button
                v-on:click="handleClick"
                class="btn btn__secondary-outline"
                style="margin-left: .5rem; margin-right: .5rem;"
                type="button"
            >
                Wyślij kod ponownie
            </button>
        </div>
    </form>
</template>
<script>
import CodeInput from './CodeInput.vue';
import emailService from '../services/email';


export default {
    props: {
        loginPage: {
            type: String,
            required: true
        },
        email: {
            type: String,
            required: true,
        },
        confirmAction: {
            type: String,
            required: true,
        },
        resendAction: {
            type: String,
            required: true,
        }
    },
    components: {
        CodeInput
    },
    data() {
        return {
            code: '',
            invalidCode: false
        }
    },
    methods: {
        handleSubmit() {
            var { email, code, confirmAction, loginPage } = this;

            if ( code.length === 0 ) return;

            emailService.confirmEmail( 
                confirmAction, 
                { email, code },
                {
                    successHandler: () => window.location = loginPage,
                    errorHandler: () => this.invalidCode = true
                }
            )
        },
        handleClick() {
            var { email, resendAction } = this;

            emailService.resendConfirmEmail( resendAction, { email } );
        },
        setCodeValue( code ) { this.code = code; },
        handleChange() { this.invalidCode = false; }
    }
}
</script>