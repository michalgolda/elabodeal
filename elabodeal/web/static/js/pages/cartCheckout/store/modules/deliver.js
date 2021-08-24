import { appData } from '@/utils/data'
import { uiModuleTypes } from './ui'
import { checkoutSessionService } from '@/services'
import { createNamespacedTypes } from '@/utils/store'


const state = () => {
	const { delivery } = appData;
	
	return {
		delivery: delivery ? delivery : {}
	}
}

const mutationTypes = {
	SET_DELIVERY: 'SET_DELIVERY'
}

const mutations = {
	[mutationTypes.SET_DELIVERY] (state, delivery) {
		state.delivery = delivery
	}
}

const getterTypes = {
	GET_EMAIL: 'GET_EMAIL',
	GET_FIRST_NAME: 'GET_FIRST_NAME',
	GET_LAST_NAME: 'GET_LAST_NAME',
	GET_DELIVERY: 'GET_DELIVERY',
	GET_DELIVERY_EMAIL: 'GET_DELIVERY_EMAIL'
}

const getters = {
	[getterTypes.GET_EMAIL] (state) {
		return state.delivery.email
	},
	[getterTypes.GET_FIRST_NAME] (state) {
		return state.delivery.first_name
	},
	[getterTypes.GET_LAST_NAME] (state) {
		return state.delivery.last_name
	},
	[getterTypes.GET_DELIVERY] (state) {
		return state.delivery
	},
	[getterTypes.GET_DELIVERY_EMAIL] (state) {
		return state.delivery.email
	}
}

const actionTypes = {
	UPDATE_DELIVER_DATA: 'UPDATE_DELIVER_DATA'
}

const actions = {
	[actionTypes.UPDATE_DELIVER_DATA] (ctx, { firstName, lastName, email }) {
		const data = new FormData()

		data.append('email', email)
		data.append('last_name', lastName)
		data.append('first_name', firstName)
	
		checkoutSessionService.updateSession(data, {
			successCallback: ({ data }) => {
				const { delivery } = data

				ctx.commit(
					mutationTypes.SET_DELIVERY,
					delivery,
					{ root: true }
				)
				
				ctx.commit(
					uiModuleTypes.mutations.SET_CURRENT_STEP, 
					'payment', 
					{ root: true }
				)
			},
			errorCallback: (errorRes) => {
				ctx.commit(
					uiModuleTypes.mutations.SHOW_ERRORS,
					errorRes.data.error.details,
					{ root:true }
				);
			}
		});
	}
}

export const deliveryModuleTypes = createNamespacedTypes('delivery', {
	getters: getterTypes,
	actions: actionTypes,
	mutations: mutationTypes
})

const deliveryModule = {
	state,
	getters,
	actions,
	mutations,
	namespaced: true
}

export default deliveryModule