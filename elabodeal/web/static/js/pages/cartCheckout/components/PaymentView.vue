<template>
	<BaseView>
		<ProductSummaryList />
		<div class="form-wrapper">
			<form 
				@submit.prevent="confirmCardPayment"
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
							type="text" 
							name="first_name" 
							ref="firstNameInputRef"
							:value="delivery.first_name"
							required
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
							type="text" 
							name="last_name" 
							ref="lastNameInputRef"
							:value="delivery.last_name"
							required
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
						type="text" 
						name="email"
						ref="emailInputRef"
						:value="delivery.email"
						required
					>
				</div>
				<div>
					<label>NUMER TELEFONU</label>
					<p 
						class="form__input-error-msg"
						v-for="error in phoneNumberErrors"
						:key="error"
					>
						{{ error }}
					</p>
					<input 
						type="text" 
						name="phone_number"
						ref="phoneNumberInputRef"
						:value="delivery.phone_number"
						oninput="this.value = this.value.replace(/[^0-9.]/g, '').replace(/(\..*)\./g, '$1');"
						required
					>
				</div>
				<div>
					<label>Numer karty</label>
					<div 
						class="StripeElementWrapper"
						:class="{ 'form__input-error': cardNumberErrors }"
					>
						<div ref="cardNumberMountElmRef" />
					</div>
				</div>
				<div class="form__section">
					<div>
						<label>Ważność karty</label>
						<div 
							class="StripeElementWrapper"
							:class="{ 'form__input-error': cardExpiryErrors }"
						>
							<div ref="cardExpiryMountElmRef" />
						</div>
					</div>
					<div>
						<label>Kod CVC</label>
						<div 
							class="StripeElementWrapper"
							:class="{ 'form__input-error': cardCvcErrors }"
						>
							<div ref="cardCvcMountElmRef" />
						</div>
					</div>
				</div>
				<div>
					<div class="flex-center">
						<img
							width="120"
							src="/static/images/stripe.png"
						>
					</div>
					<div class="form__input-checkbox">
						<input 
							type="checkbox" 
							required="required"
						>
						<label>Akceptuje regulamin</label>
					</div>
					<div class="form__input-checkbox">
						<input 
							type="checkbox" 
							required="required"
						>
						<label>Akceptuje politykę prywatnośći</label>
					</div>
				</div>
				<button 
					class="btn btn__primary btn-block"
					type="submit"
				>
					Zamawiam i płacę
				</button>
				<button
					class="btn btn__secondary btn-block"
					type="button"
					@click="backToDeliverView"
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
import { useStripe } from '../hooks'
import { actionsTypes } from '../store/actions'
import { mutationsTypes } from '../store/mutations'

import BaseView from './BaseView'
import ProductSummaryList from './ProductSummaryList'


export default {
	components: {
		BaseView,
		ProductSummaryList
	},
	setup () {
		const store = useStore()

		const stripePublishableKey = store.state.stripePublishableKey

		const paymentIntentClientSecret = store.state.paymentIntentClientSecret

		const paymentSuccessCallback = (_, payerFirstName) => {
			store.dispatch(
				actionsTypes.SUCCEED_CHECKOUT_SESSION,
				{ firstName: payerFirstName }
			)
		}

		const stripeErrors = ref({})

		const paymentErrorCallback = (error) => {
			const errorCode = error.code
			const errorMessage = error.message
			const errorInput = errorCode.substr(errorCode.indexOf('_') + 1)

			stripeErrors.value[errorInput] = errorMessage

			console.log(stripeErrors)
		}

		const { 
			emailInputRef,
			phoneNumberInputRef,
			lastNameInputRef,
			firstNameInputRef,
			confirmCardPayment,
			cardCvcMountElmRef,
			cardNumberMountElmRef,
			cardExpiryMountElmRef
		} = useStripe(
			stripePublishableKey,
			paymentIntentClientSecret,
			{ 
				paymentSuccessCallback, 
				paymentErrorCallback
			}
		)

		const delivery = computed(() => {
			return store.state.delivery
		})

		const backToDeliverView = () => {
			store.commit(
				mutationsTypes.SET_CURRENT_STEP,
				'deliver'
			)
		}

		const firstNameErrors = computed(() => {
			return store.state.errors.first_name
		})

		const lastNameErrors = computed(() => {
			return store.state.errors.last_name
		})

		const emailErrors = computed(() => {
			return store.state.errors.email
		})

		const phoneNumberErrors = computed(() => {
			return store.state.errors.phone_number
		})

		const cardCvcErrors = computed(() => {
			return stripeErrors.value.cvc
		})

		const cardNumberErrors = computed(() => {
			return stripeErrors.value.number
		})

		const cardExpiryErrors = computed(() => {
			return stripeErrors.value.expiry
		})

		return {
			stripeErrors,
			delivery,
			emailInputRef,
			backToDeliverView,
			confirmCardPayment,
			phoneNumberInputRef,
			firstNameInputRef,
			lastNameInputRef,
			cardCvcMountElmRef,
			cardNumberMountElmRef,
			cardExpiryMountElmRef,
			firstNameErrors,
			lastNameErrors,
			emailErrors,
			phoneNumberErrors,
			cardCvcErrors,
			cardNumberErrors,
			cardExpiryErrors
		}
	}
}
</script>