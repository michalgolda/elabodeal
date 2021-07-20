import { appData } from '@/utils/data';
import cartService from '@/services/cart';


const initialState = () => {
	const { 
		checkout_session: checkoutSession,
		summary_products: summaryProducts,
		summary_total_price: summaryTotalPrice,
		stripe_publishable_key: stripePublishableKey } = appData;

	const paymentIntentClientSecret = checkoutSession['cs'];

	return {
		payment: {},
		summaryProducts,
		summaryTotalPrice,
		stripePublishableKey,
		paymentIntentClientSecret
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