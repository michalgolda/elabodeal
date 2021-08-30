<template>
	<BaseView>
		<div class="form-wrapper">
			<form 
				@submit.prevent="updateDeliverData" 
				class="form"
				autocomplete="off" 
			>
				<div class="form__section">
					<div>
						<label>IMIĘ</label>
						<p
							class="form__input-error-msg"
							v-for="error in firstNameErrors"
							:key="error"
						>
							{{ error }}
						</p>
						<input 
							name="first_name"
							type="text"
							required="required"
							:value="firstName"
							ref="firstNameInputRef"
						>
					</div>
					<div>
						<label>NAZWISKO</label>
						<p
							class="form__input-error-msg"
							v-for="error in lastNameErrors"
							:key="error"
						>
							{{ error }}
						</p>
						<input 
							name="last_name"
							type="text"
							required="required"
							:value="lastName"
							ref="lastNameInputRef" 
						>
					</div>
				</div>
				<div>
					<label>E-MAIL</label>
					<p
						class="form__input-error-msg"
						v-for="error in emailErrors"
						:key="error"
					>
						{{ error }}
					</p>
					<input 
						name="email"
						type="email"
						required="required"
						:value="email"
						ref="emailInputRef" 
					>
				</div>
				<button 
					class="btn btn__primary btn-block"
					type="submit" 
				>
					Przejdź dalej
				</button>
				<button 
					class="btn btn__secondary btn-block"
					type="button"
					@click="cancelCheckoutSession"
				>
					Wstecz
				</button>
			</form>
		</div>
	</BaseView>
</template>
<script>
import { computed, ref } from 'vue'
import { useStore } from 'vuex'
import { actionsTypes } from '../store/actions'

import BaseView from './BaseView'


export default {
	components: {
		BaseView
	},
	setup () {
		const store = useStore()

		const email = computed(() => {
			return store.state.delivery.email
		})

		const firstName = computed(() => {
			return store.state.delivery.firstName
		})

		const lastName = computed(() => {
			return store.state.delivery.lastName
		})

		const emailErrors = computed(() => {
			return store.state.errors.email
		})
		
		const firstNameErrors = computed(() => {
			return store.state.errors.first_name
		})

		const lastNameErrors = computed(() => {
			return store.state.errors.last_name
		})

		const emailInputRef = ref(null)
		const lastNameInputRef = ref(null)
		const firstNameInputRef = ref(null)

		const updateDeliverData = () => {
			const emailInput = emailInputRef.value
			const lastNameInput = lastNameInputRef.value
			const firstNameInput = firstNameInputRef.value

			store.dispatch(
				actionsTypes.UPDATE_CHECKOUT_SESSION,
				{
					email: emailInput.value,
					lastName: lastNameInput.value,
					firstName: firstNameInput.value
				}
			)
		}

		const cancelCheckoutSession = () => {
			store.dispatch(actionsTypes.CANCEL_CHECKOUT_SESSION)
		}

		return {
			email,
			lastName,
			firstName,
			emailErrors,
			lastNameErrors,
			firstNameErrors,
			emailInputRef,
			lastNameInputRef,
			firstNameInputRef,
			updateDeliverData,
			cancelCheckoutSession
		}
	}
}
</script>