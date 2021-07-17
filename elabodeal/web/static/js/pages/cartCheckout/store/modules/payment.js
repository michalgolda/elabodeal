import cartService from '@/services/cart';


const initialState = () => {
	const stripePublishableKey = window.__APP_CONTEXT__['stripe_publishable_key'];

	const checkoutSession = window.__APP_CONTEXT__['checkout_session'];
	const paymentIntentClientSecret = checkoutSession['cs'];

	return {
		stripePublishableKey,
		paymentIntentClientSecret,
		payment: {}
	}
};

const paymentModule = {
	namespaced: true,
	state: initialState(),
	mutations: {
		setPaymentData (state, data) {
			state.payment = data;
		}
	},
	actions: {
		succeedCheckoutSession (ctx) {
			cartService.succeedCheckoutSession(null, {
				successCallback: () => {
					ctx.commit(
						'ui/setCurrentStep',
						'success',
						{root:true}
					)
				}
			})
		}
	}
};

export default paymentModule;