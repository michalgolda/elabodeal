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
import { ref } from 'vue'
import { useStore } from 'vuex'
import { mainModuleTypes } from '../store/modules'


export default {
    setup () {
        const store = useStore()

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
            startResetPasswordFlow
        }
    }
}
</script>