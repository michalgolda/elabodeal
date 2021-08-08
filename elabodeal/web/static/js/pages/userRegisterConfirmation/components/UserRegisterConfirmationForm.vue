<template>
    <div class="section">
        <h2>
            Zweryfikuj swoje konto
        </h2>
        <p>
            Aby zweryfikować konto należy podać kod weryfikacyjny wysłany
            na podany adres email <strong>{{ email }}</strong>. 
        </p>
        <code-input
           :class="{ 'code-invalid': codeErrors }"
            @complete="handleComplete"
        />
        <div class="flex-center">
            <button
                class="btn btn__secondary-outline"
                type="button"
                @click="handleResendCode"
            >
                Wyślij kod ponownie
            </button>
        </div>
    </div>
</template>
<script>
import { mapState, mapActions } from 'vuex';
import CodeInput from '@/components/CodeInput';


export default {
    components: {
        CodeInput
    },
    computed: mapState({
        email: state => state.email,
        code: state => state.code,
        codeErrors: state => state.error.code
    }),
    mounted () {
        if (this.email && this.code)
            this.registerConfirmation({
                code: this.code,
                email: this.email
            });
    },
    methods: {
        ...mapActions([
            'registerConfirmation',
            'resendRegisterConfirmation'
        ]),
        handleComplete (code) {
            this.registerConfirmation({
                code,
                email: this.email
            });
        },
        handleResendCode () {
            this.resendRegisterConfirmation({
                email: this.email
            });
        }
    }
}
</script>