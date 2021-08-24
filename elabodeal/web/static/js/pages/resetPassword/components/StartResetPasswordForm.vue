<template>
    <div class="informations">
        <h2>Zresetuj swoje hasło</h2>
        <p>Miejsce na informację dotyczącą procesu resetowania hasła</p>
    </div>
    <form 
        @submit.prevent="startResetPasswordFlow" 
        class="form"
    >
        <div class="form__input-group">
            <label>Adres email powiązany z kontem</label>
            <p 
                class="form__input-error-msg"
                v-for="error in emailErrors"
                :key="error"
            >
                {{ error }}
            </p>
            <input 
                ref="emailInputRef" 
                type="text" 
                name="email" 
                required 
            >
        </div>
        <button class="btn btn__secondary btn-block">
            Dalej
        </button>
    </form>
</template>
<script>
import { ref, computed } from 'vue'
import { useStore } from 'vuex'
import { uiModuleTypes, mainModuleTypes } from '../store/modules'


export default {
    setup () {
        const store = useStore()

        const emailErrors = computed(() => {
            return store.getters[uiModuleTypes.getters.GET_EMAIL_ERRORS]
        })

        const emailInputRef = ref(null)

        const startResetPasswordFlow = () => {
            const emailInput = emailInputRef.value;

            store.dispatch(
                mainModuleTypes.actions.START_RESET_PASSWORD_FLOW,
                { email: emailInput.value }
            )
        }

        return {
            emailInputRef,
            emailErrors,
            startResetPasswordFlow
        }
    }
}
</script>