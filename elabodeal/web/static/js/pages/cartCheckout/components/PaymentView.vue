<template>
	<BaseView>
		<ProductSummaryList />
		<div class="form-wrapper">
			<form 
				@submit.prevent="handleSubmit"
				class="form"
				autocomplete="off"
			>
				<div class="form__section">
					<div>
						<label>IMIĘ</label>
						<input 
							type="text" 
							name="first_name" 
							ref="first_name"
							:value="delivery.first_name"
							required
						>
					</div>
					<div>
						<label>NAZWISKO</label>
						<input 
							type="text" 
							name="last_name" 
							ref="last_name"
							:value="delivery.last_name"
							required
						>
					</div>
				</div>
				<div>
					<label>E-MAIL</label>
					<input 
						type="text" 
						name="email"
						ref="email"
						:value="delivery.email"
						required
					>
				</div>
				<div>
					<label>NUMER TELEFONU</label>
					<input 
						type="text" 
						name="phone_number"
						ref="phone_number"
						:value="delivery.phone_number"
						oninput="this.value = this.value.replace(/[^0-9.]/g, '').replace(/(\..*)\./g, '$1');"
						required
					>
				</div>
				<div>
					<label>Numer karty</label>
					<div class="StripeElementWrapper">
						<div ref="stripeCardNumber" />
					</div>
				</div>
				<div class="form__section">
					<div>
						<label>Ważność karty</label>
						<div class="StripeElementWrapper">
							<div ref="stripeCardExpiry" />
						</div>
					</div>
					<div>
						<label>Kod CVC</label>
						<div class="StripeElementWrapper">
							<div ref="stripeCardCvc" />
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
					@click="() => setCurrentStep('deliver')"
				>
					Wstecz
				</button>
			</form>
		</div>
	</BaseView>
</template>
<script>
import { createNamespacedHelpers } from 'vuex';
import Alert from '@/alert';

import BaseView from './BaseView';
import ProductSummaryList from './ProductSummaryList';

const { mapMutations: mapUiMutations } = createNamespacedHelpers('ui');
const { mapState: mapDeliverState } = createNamespacedHelpers('deliver');
const { 
	mapState: mapPaymentState,
	mapActions: mapPaymentActions,
	mapMutations: mapPaymentMutations } = createNamespacedHelpers('payment');


export default {
	components: {
		BaseView,
		ProductSummaryList
	},
	computed: {
		...mapDeliverState(['delivery']),
		...mapPaymentState([
			'stripePublishableKey',
			'paymentIntentClientSecret'
		])
	},
	mounted () {
		// eslint-disable-next-line
		this.stripe = Stripe(this.stripePublishableKey);
		this.stripeElements = this.stripe.elements();
		
		const defaultOptions = {
			style: {
				base: {
					color: '#011627',
					fontWeight: 500,
					fontFamily: 'Montserrat, Open Sans, Segoe UI, sans-serif',
					fontSize: '15.5px'
				},
				invalid: {
					iconColor: '#E71D36',
					color: '#E71D36'
				}
			}
		};

		this.stripeCardCvc = this.stripeElements.create('cardCvc', defaultOptions);
		this.stripeCardNumber = this.stripeElements.create('cardNumber', defaultOptions);
		this.stripeCardExpiry = this.stripeElements.create('cardExpiry', defaultOptions);

		const { 
			stripeCardCvc: mountStripeCardCvc,
			stripeCardNumber: mountStripeCardNumber,
			stripeCardExpiry: mountStripeCardExpiry } = this.$refs;

		this.stripeCardCvc.mount(mountStripeCardCvc);
		this.stripeCardExpiry.mount(mountStripeCardExpiry);
		this.stripeCardNumber.mount(mountStripeCardNumber);
	},
	data () {
		return {
			cardErrors: []
		}
	},
	methods: {
		...mapUiMutations(['setCurrentStep']),
		...mapPaymentMutations(['setPaymentData']),
		...mapPaymentActions(['succeedCheckoutSession']),
		handleSubmit () {
			const { 
				first_name, 
				last_name, 
				email, 
				phone_number } = this.$refs;

			this.cardErrors = [];

			this.stripe
				.confirmCardPayment(this.paymentIntentClientSecret, {
					payment_method: {
						card: this.stripeCardNumber,
						billing_details: {
							email: email.value,
							phone: phone_number.value,
							name: `${first_name.value} ${last_name.value}`
						}
					}
				})
				.then(result => {
					result.error ? (
						this.handlePaymentError(result.error)
					) : (
						this.handlePaymentSuccess(result.paymentIntent)
					);
				})
		},
		handlePaymentError (error) {
			const errorType = error.type;

			switch (errorType) {
				case 'validation_error':
					this.cardErrors.pop();
					this.cardErrors.push('Wprowadzono błędne dane');

					break;
				case 'invalid_request_error':
					Alert.info('Wystąpił błąd podczas przetwarzania płatności. Spróbuj ponwonie.');

					break;
			}
		},
		handlePaymentSuccess () {
			const { first_name } = this.$refs;

			this.setPaymentData({ first_name: first_name.value });

			this.succeedCheckoutSession();
		}
	}
}
</script>