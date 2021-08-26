import { getApplicationData } from '@/utils/data'
import { uiModuleTypes } from './ui'
import { checkoutSessionService } from '@/services'
import { createNamespacedTypes } from '@/utils/store'


const state = () => {
	const { 
		checkout_session: checkoutSession,
		summary_products: summaryProducts,
		summary_total_price: summaryTotalPrice,
		stripe_publishable_key: stripePublishableKey } = getApplicationData()

	const paymentIntentClientSecret = checkoutSession['cs']

	return {
		payerFirstName: '',
		summaryProducts,
		summaryTotalPrice,
		stripePublishableKey,
		paymentIntentClientSecret
	}
}

const mutationTypes = {
	SET_PAYER_FIRST_NAME: 'SET_PAYER_FIRST_NAME'
}

const mutations = {
	[mutationTypes.SET_PAYER_FIRST_NAME] (state, payerFirstName) {
		state.payerFirstName = payerFirstName
	}
}

const getterTypes = {
	GET_SUMMARY_PRODUCTS: 'GET_SUMMARY_PRODUCTS',
	GET_SUMMARY_TOTAL_PRICE: 'GET_SUMMARY_TOTAL_PRICE',
	GET_PAYER_FIRST_NAME: 'GET_PAYER_FIRST_NAME',
	GET_STRIPE_PUBLISHABLE_KEY: 'GET_STRIPE_PUBLISHABLE_KEY',
	GET_PAYMENT_INTENT_CLIENT_SECRET: 'GET_PAYMENT_INTENT_CLIENT_SECRET'
}

const getters = {
	[getterTypes.GET_PAYER_FIRST_NAME] (state) {
		return state.payerFirstName
	},
	[getterTypes.GET_SUMMARY_PRODUCTS] (state) {
		return state.summaryProducts
	},
	[getterTypes.GET_SUMMARY_TOTAL_PRICE] (state) {
		return state.summaryTotalPrice
	},
	[getterTypes.GET_STRIPE_PUBLISHABLE_KEY] (state) {
		return state.stripePublishableKey
	},
	[getterTypes.GET_PAYMENT_INTENT_CLIENT_SECRET] (state) {
		return state.paymentIntentClientSecret
	}
}	

const actionTypes = {
	SUCCEED_CHECKOUT_SESSION: 'SUCCEED_CHECKOUT_SESSION'
}

const actions = {
	[actionTypes.SUCCEED_CHECKOUT_SESSION] (ctx, { firstName }) {
		checkoutSessionService.succeedSession(null, {
			successCallback: () => {
				ctx.commit(
					uiModuleTypes.mutations.SET_CURRENT_STEP,
					'success',
					{ root: true }
				)

				ctx.commit(
					mutationTypes.SET_PAYER_FIRST_NAME,
					firstName,
					{ root: true }
				)
			}
		})
	}
}

export const paymentModuleTypes = createNamespacedTypes('payment', {
	getters: getterTypes,
	actions: actionTypes,
	mutations: mutationTypes
})

const paymentModule = {
	state,
	actions,
	getters,
	mutations,
	namespaced: true
}

export default paymentModule;