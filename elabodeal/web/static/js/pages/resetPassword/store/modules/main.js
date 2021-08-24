import { uiModuleTypes } from './ui'
import { userService } from '@/services'
import { setCurrentUrlParam } from '@/utils/url'
import { createNamespacedTypes } from '@/utils/store'


const state = () => {
    return { email: null }
}

const mutationTypes = {
    SET_EMAIL: 'SET_EMAIL'
}

const mutations = {
    [mutationTypes.SET_EMAIL] (state, email) {
        state.email = email ? email : null
    }
}

const getterTypes = {
    GET_EMAIL: 'GET_EMAIL'
}

const getters = {
    [getterTypes.GET_EMAIL] (state) {
        return state.email
    }
}

const actionTypes = {
    START_RESET_PASSWORD_FLOW: 'START_RESET_PASSWORD_FLOW',
    END_RESET_PASSWORD_FLOW: 'END_RESET_PASSWORD_FLOW'
}

const actions = {
    [actionTypes.START_RESET_PASSWORD_FLOW] (ctx, { email }) {
        const data = new FormData()

        data.append('email', email)

        userService.startResetPasswordFlow(data, {
            successCallback: () => {
                setCurrentUrlParam('email', email);

                ctx.commit(mutationTypes.SET_EMAIL, email, {root: true})
                ctx.commit(uiModuleTypes.mutations.SET_STEP, 'end', {root: true})
            },
            errorCallback: (errorRes) => {
                ctx.commit(
                    uiModuleTypes.mutations.SHOW_ERRORS,
                    errorRes.data.error.details,
                    {root: true}
                )
            }
        })
    },
    [actionTypes.END_RESET_PASSWORD_FLOW] (
        _, 
        { 
            email, 
            code, 
            newPasswordOne, 
            newPasswordTwo 
        }
    ) {
        const data = new FormData()

        data.append('code', code)
        data.append('email', email)
        data.append('new_password1', newPasswordOne)
        data.append('new_password2', newPasswordTwo)

        userService.endResetPasswordFlow(data, {
            successCallback: () => {
                window.location = '/login/';
            }
        })
    }
}

export const mainModuleTypes = createNamespacedTypes('main', {
    getters: getterTypes,
    actions: actionTypes,
    mutations: mutationTypes
})

const mainModule = {
    state,
    actions,
    getters,
    mutations,
    namespaced: true
}

export default mainModule;