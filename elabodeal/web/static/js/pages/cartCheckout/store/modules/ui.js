import { getApplicationData } from '@/utils/data'
import { deliveryModuleTypes } from './deliver'
import { createNamespacedTypes } from '@/utils/store'


const state = () => {
	const { checkout_session: checkoutSession } = getApplicationData()

	const { step } = checkoutSession

	return {
		errors: {},
		currentStep: step ? step : 'deliver'
	}
}

const mutationTypes = {
	SHOW_ERRORS: 'SHOW_ERRORS',
	CLEAR_ERRORS: 'CLEAR_ERRORS',
	SET_CURRENT_STEP: 'SET_CURRENT_STEP'
}

const mutations = {
	[mutationTypes.SHOW_ERRORS] (state, errors) {
		state.errors = errors
	},
	[mutationTypes.CLEAR_ERRORS] (state) {
		state.errors = {}
	},
	[mutationTypes.SET_CURRENT_STEP] (state, step) {
		state.currentStep = step ? step : 'deliver'
	}
}

const getterTypes = {
	GET_CURRENT_STEP: 'GET_CURRENT_STEP',
	GET_EMAIL_ERRORS: 'GET_EMAIL_ERRORS',
	GET_FIRST_NAME_ERRORS: 'GET_FIRST_NAME_ERRORS',
	GET_LAST_NAME_ERRORS: 'GET_LAST_NAME_ERRORS',
	SHOW_DELIVER_VIEW: 'SHOW_DELIVER_VIEW',
	SHOW_PAYMENT_VIEW: 'SHOW_PAYMENT_VIEW',
	SHOW_PAYMENT_SUCCESS_VIEW: 'SHOW_PAYMENT_SUCCESS_VIEW',
	GET_CARD_CVC_ERRORS: 'GET_CARD_CVC_ERRORS',
	GET_CARD_NUMBER_ERRORS: 'GET_CARD_NUMBER_ERRORS',
	GET_CARD_EXPIRY_ERRORS: 'GET_CARD_EXPIRY_ERRORS',
	GET_PHONE_NUMBER_ERRORS: 'GET_PHONE_NUMBER_ERRORS'
}

const getters = {
	[getterTypes.GET_EMAIL_ERRORS] (state) {
		return state.errors.email
	},
	[getterTypes.GET_FIRST_NAME_ERRORS] (state) {
		return state.errors.first_name
	},
	[getterTypes.GET_LAST_NAME_ERRORS] (state) {
		return state.errors.last_name
	},
	[getterTypes.GET_CURRENT_STEP] (state) {
		return state.currentStep
	},
	[getterTypes.SHOW_DELIVER_VIEW] (state) {
		return state.currentStep === 'deliver'
	},
	[getterTypes.SHOW_PAYMENT_VIEW] (state, getters, rootState, rootGetters) {
		const hasDelivery = rootGetters[deliveryModuleTypes.getters.GET_DELIVERY] !== {}
		
		return state.currentStep === 'payment' && hasDelivery
	},
	[getterTypes.SHOW_PAYMENT_SUCCESS_VIEW] (state) {
		return state.currentStep === 'success'
	},
	[getterTypes.GET_CARD_CVC_ERRORS] (state) {
		return state.errors.cvc
	},
	[getterTypes.GET_CARD_NUMBER_ERRORS] (state) {
		return state.errors.number
	},
	[getterTypes.GET_CARD_EXPIRY_ERRORS] (state) {
		return state.errors.expiry
	},
	[getterTypes.GET_PHONE_NUMBER_ERRORS] (state) {
		return state.errors.phone_number
	}
}

export const uiModuleTypes = createNamespacedTypes('ui', {
	getters: getterTypes,
	mutations: mutationTypes
})

const uiModule = {
	state,
	getters,
	mutations,
	namespaced: true
}

export default uiModule;