import { mainModuleTypes } from './main';
import { setCurrentUrlParam } from '@/utils/url'
import { createNamespacedTypes } from '@/utils/store';


const state = () => {
    return {
        step: 'start',
        errors: {}
    }
}

const mutationTypes = {
    SET_STEP: 'SET_STEP',
    SHOW_ERRORS: 'SHOW_ERRORS'
}

const mutations = {
    [mutationTypes.SET_STEP] (state, step) {
        step = step ? step.toLowerCase() : 'start'

        setCurrentUrlParam('step', step)

        state.step = step
    },
    [mutationTypes.SHOW_ERRORS] (state, errors) {
        state.errors = errors
    }
}

const getterTypes = {
    SHOW_END_FORM: 'SHOW_END_FORM',
    GET_CODE_ERRORS: 'GET_CODE_ERRORS',
    GET_EMAIL_ERRORS: 'GET_EMAIL_ERRORS',
    GET_NEW_PASSWORD_TWO_ERRORS: 'GET_NEW_PASSWORD_TWO_ERRORS',
    GET_NEW_PASSWORD_ONE_ERRORS: 'GET_NEW_PASSWORD_ONE_ERRORS'
}

const getters = {
    [getterTypes.GET_EMAIL_ERRORS] (state) {
        return state.errors.email
    },
    [getterTypes.SHOW_END_FORM] (state, getters, rootState, rootGetters) {
        return state.step === 'end' && rootGetters[mainModuleTypes.getters.GET_EMAIL]
    },
    [getterTypes.GET_NEW_PASSWORD_ONE_ERRORS] (state) {
        return state.errors.new_password1
    },
    [getterTypes.GET_NEW_PASSWORD_TWO_ERRORS] (state ) {
        return state.errors.new_password2
    },
    [getterTypes.GET_CODE_ERRORS] (state) {
        return state.errors.code
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