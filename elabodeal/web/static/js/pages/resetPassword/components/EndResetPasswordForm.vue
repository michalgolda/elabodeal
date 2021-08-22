<template>
    <div class="informations">
        <h2>Zresetuj swoje hasło</h2>
        <p>Podaj kod bezpieczeństwa wysłany na podany adres email <strong>{{ email }}</strong></p>
    </div>
    <form @submit.prevent="handleSubmit" class="form">
        <div class="form__input-group">
            <label>Kod bezpieczeństwa</label>
            <p 
                class="form__input-error-msg"
                v-for="error in codeErrors"
                :key="error"
            >
                {{ error }}
            </p>
            <input ref="codeInput" type="text" name="code" required/>
        </div>
        <div class="form__input-group">
            <label>Nowe hasło</label>
            <p 
                class="form__input-error-msg"
                v-for="error in newPassword1Errors"
                :key="error"
            >
                {{ error }}
            </p>
            <input ref="newPassword1Input" type="password" name="new_password1" required/>
        </div>
        <div class="form__input-group">
            <label>Powtórz nowe hasło</label>
            <p 
                class="form__input-error-msg"
                v-for="error in newPassword2Errors"
                :key="error"
            >
                {{ error }}
            </p>
            <input ref="newPassword2Input" type="password" name="new_password2" required/>
        </div>
        <div class="form__input-group">
            <button class="btn btn__secondary btn-block" type="submit">Zmień</button>
        </div>
        <button @click="handleResendCode" class="btn btn__primary btn-block" type="button">Wyślij kod ponownie</button>
    </form>
</template>
<script>
import { 
    mapState as mapRootState,
    mapActions as mapRootActions,
    createNamespacedHelpers } from 'vuex'

const { mapState: mapUiState } = createNamespacedHelpers('ui');


export default {
    computed: {
        ...mapRootState(['email']),
        ...mapUiState({
            codeErrors: state => state.errors.code,
            newPassword1Errors: state => state.errors.new_password1,
            newPassword2Errors: state => state.errors.new_password2 
        })
    },
    methods: {
        ...mapRootActions([
            'startResetPasswordFlow',
            'endResetPasswordFlow'
        ]),
        handleSubmit () {
            const { 
                codeInput,
                newPassword1Input,
                newPassword2Input } = this.$refs;

            this.endResetPasswordFlow({
                email: this.email,
                code: codeInput.value,
                newPassword1: newPassword1Input.value,
                newPassword2: newPassword2Input.value
            })
        },
        handleResendCode () {
            this.startResetPasswordFlow({
                email: this.email
            })
        }
    }
}
</script>