<template>
    <form 
        @submit.prevent="handleSubmitForm"
        class="form"
    >
        <div class="form__group form__group-col-2">
            <div class="form__inputContainer">
                <label>Imię</label>
                <p 
					class="form__input-error-msg"
					v-for="error in firstNameErrors"
					:key="error"
				>
					{{ error }}
				</p>
                <input
                    ref="firstName"
                    class="form__input"
                    type="text" 
                    name="first_name"
                    required
                >
            </div>
            <div class="form__inputContainer">
                <label>Nazwisko</label>
                <p 
					class="form__input-error-msg"
					v-for="error in lastNameErrors"
					:key="error"
				>
					{{ error }}
				</p>
                <input
                    ref="lastName"
                    class="form__input"
                    type="text" 
                    name="last_name"
                    required
                >
            </div>
        </div>
        <div class="form__inputContainer">
            <label>Kraj</label>
            <select ref="country">
                <option
                    v-for="country in supportedCountries"
                    :key="country"
                >
                    {{ country }}
                </option>  
            </select>
        </div>
        <div class="form__inputContainer">
            <label>Numer konta</label>
            <p 
                class="form__input-error-msg"
                v-for="error in accountNumberErrors"
                :key="error"
            >
                {{ error }}
            </p>
            <input
                ref="accountNumber"
                class="form__input"
                type="text" 
                name="account_number"
                required
            >
        </div>
        <div class="form__inputContainer">
            <label>Swift</label>
            <p 
                class="form__input-error-msg"
                v-for="error in swiftErrors"
                :key="error"
            >
                {{ error }}
            </p>
            <input
                ref="swift"
                class="form__input"
                type="text" 
                name="swift"
                required
            >
        </div>
        <div class="form__inputContainer">
            <button class="btn btn__secondary btn-block">
                Zakładam konto
            </button>
        </div>
        <div class="form__inputContainer">
            <button 
                @click="handleBack"
                class="btn btn__primary-outline btn-block"
            >
                Wróć
            </button>
        </div>
    </form>
</template>
<script>
import { 
    mapState as mapRootState,
    mapActions as mapRootActions,
    createNamespacedHelpers } from 'vuex';


const { 
    mapState: mapUiState,
    mapMutations: mapUiMutations } = createNamespacedHelpers('ui');


export default {
    computed: {
        ...mapRootState(['supportedCountries']),
        ...mapUiState({
            firstNameErrors: state => state.errors.first_name,
            lastNameErrors: state => state.errors.last_name,
            accountNumberErrors: state => state.errors.account_number,
            swiftErrors: state => state.errors.swift
        })
    },
    methods: {
        ...mapRootActions(['createPublisher']),
        ...mapUiMutations(['setFormType']),
        handleSubmitForm () {
            const { 
                firstName,
                lastName,
                accountNumber,
                country,
                swift } = this.$refs;

            this.createPublisher({
                country: country.value,
                lastName: lastName.value,
                firstName: firstName.value,
                swift: swift.value,
                accountNumber: accountNumber.value
            });
        },
        handleBack () {
            this.setFormType(null);
        }
    }
}
</script>
