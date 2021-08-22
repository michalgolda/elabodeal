<template>
    <div class="informations">
        <h2>Zresetuj swoje hasło</h2>
        <p>Miejsce na informację dotyczącą procesu resetowania hasła</p>
    </div>
    <form @submit.prevent="handleSubmit" class="form">
        <div class="form__input-group">
            <label>Adres email powiązany z kontem</label>
            <p 
                class="form__input-error-msg"
                v-for="error in emailErrors"
                :key="error"
            >
                {{ error }}
            </p>
            <input ref="emailInput" type="text" name="email" />
        </div>
        <button class="btn btn__secondary btn-block">Dalej</button>
    </form>
</template>
<script>
import { mapActions as mapRootActions, createNamespacedHelpers } from 'vuex'

const { mapState: mapUiState } = createNamespacedHelpers('ui');


export default {
    computed: mapUiState({
        emailErrors: state => state.errors.email
    }),
    methods: {
        ...mapRootActions(['startResetPasswordFlow']),
        handleSubmit () {
            const { emailInput } = this.$refs;
            
            this.startResetPasswordFlow({
                email: emailInput.value
            })
        }
    },
}
</script>