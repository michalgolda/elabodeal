<template>
    <div class="informations">
        <h2>Zresetuj swoje hasło</h2>
        <p>Podaj kod weryfikacyjny wysłany na podany adres email <strong>{{ email }}</strong></p>
    </div>
    <form @submit.prevent="endResetPasswordFlow" class="form">
        <div class="form__input-group">
            <label>Kod weryfikacyjny</label>
            <p 
                class="form__input-error-msg"
                v-for="error in codeErrors"
                :key="error"
            >
                {{ error }}
            </p>
            <input ref="codeInputRef" type="text" name="code" required/>
        </div>
        <div class="form__input-group">
            <label>Nowe hasło</label>
            <p 
                class="form__input-error-msg"
                v-for="error in newPasswordOneErrors"
                :key="error"
            >
                {{ error }}
            </p>
            <input ref="newPasswordOneInputRef" type="password" name="new_password1" required/>
        </div>
        <div class="form__input-group">
            <label>Powtórz nowe hasło</label>
            <p 
                class="form__input-error-msg"
                v-for="error in newPasswordTwoErrors"
                :key="error"
            >
                {{ error }}
            </p>
            <input ref="newPasswordTwoInputRef" type="password" name="new_password2" required/>
        </div>
        <div class="form__input-group">
            <button class="btn btn__secondary btn-block" type="submit">Zmień</button>
        </div>
        <button @click="startResetPasswordFlow" class="btn btn__primary btn-block" type="button">Wyślij kod ponownie</button>
    </form>
</template>
<script>
import { ref, computed } from 'vue'
import { useStore } from 'vuex'
import { uiModuleTypes, mainModuleTypes } from '../store/modules'

export default {
    setup () {
        const store = useStore()

        const email = computed(() => {
            return store.getters[mainModuleTypes.getters.GET_EMAIL]
        })

        const codeErrors = computed(() => {
            return store.getters[uiModuleTypes.getters.GET_CODE_ERRORS]
        })

        const newPasswordOneErrors = computed(() => {
            return store.getters[uiModuleTypes.getters.GET_NEW_PASSWORD_ONE_ERRORS]
        })

        const newPasswordTwoErrors = computed(() => {
            return store.getters[uiModuleTypes.getters.GET_NEW_PASSWORD_TWO_ERRORS]
        })

        const startResetPasswordFlow = () => {
            store.dispatch(
                mainModuleTypes.actions.START_RESET_PASSWORD_FLOW,
                { email: email.value }
            )
        }

        const codeInputRef = ref(null)
        const newPasswordOneInputRef = ref(null)
        const newPasswordTwoInputRef = ref(null)

        const endResetPasswordFlow = () => {
            const codeInput = codeInputRef.value;
            const newPasswordOneInput = newPasswordOneInputRef.value;
            const newPasswordTwoInput = newPasswordTwoInputRef.value;

            store.dispatch(
                mainModuleTypes.actions.END_RESET_PASSWORD_FLOW,
                {
                    email: email.value,
                    code: codeInput.value,
                    newPasswordOne: newPasswordOneInput.value,
                    newPasswordTwo: newPasswordTwoInput.value
                }
            )
        }

        return {
            email,
            codeErrors,
            codeInputRef,
            newPasswordTwoErrors,
            newPasswordOneErrors,
            endResetPasswordFlow,
            startResetPasswordFlow,
            newPasswordOneInputRef,
            newPasswordTwoInputRef
        }
    }
}
</script>