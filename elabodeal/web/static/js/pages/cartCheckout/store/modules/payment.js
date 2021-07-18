import cartService from '@/services/cart';


const initialState = () => {
	const stripePublishableKey = window.__APP_CONTEXT__['stripe_publishable_key'];

	const checkoutSession = window.__APP_CONTEXT__['checkout_session'];
	const paymentIntentClientSecret = checkoutSession['cs'];
	const summaryProducts = window.__APP_CONTEXT__['summary_products'];
	const summaryTotalPrice = window.__APP_CONTEXT__['summary_total_price'];

	return {
		stripePublishableKey,
		paymentIntentClientSecret,
		summaryProducts,
		summaryTotalPrice,
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