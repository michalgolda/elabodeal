import { createNamespacedTypes } from '@/utils/store'


const state = () => {
	return {
		errors: {}
	}
}

const mutationTypes = {
	SHOW_ERRORS: 'SHOW_ERRORS'
}

const mutations = {
	[mutationTypes.SHOW_ERRORS] (state, errors) {
		state.errors = errors
	}
}

const getterTypes = {
	GET_TITLE_ERRORS: 'GET_TITLE_ERRORS',
	GET_DESCRIPTION_ERRORS: 'GET_DESCRIPTION_ERRORS'
}

const getters = {
	[getterTypes.GET_TITLE_ERRORS] (state)  {
		return state.errors.title
	},
	[getterTypes.GET_DESCRIPTION_ERRORS] (state) {
		return state.errors.description
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