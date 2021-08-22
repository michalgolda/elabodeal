import { createStore } from 'vuex'
import { getUrlParam, setCurrentUrlParam } from '@/utils/url'
import { userService } from '@/services'

import { uiModule } from './modules'


const initialState = () => {
    const email = getUrlParam('email')
    
    return {
        email: email ? email : null
    }
}

const store = createStore({
    namespaced: true,
    state: initialState(),
    modules: {
        ui: uiModule
    },
    mutations: {
        setEmail (state, email) {
            setCurrentUrlParam('email', email);

            state.email = email;
        }
    },
    actions: {
        startResetPasswordFlow (ctx, { email }) {
            const data = new FormData()

            data.append('email', email)

            userService.startResetPasswordFlow(data, {
                successCallback: () => {
                    ctx.commit('setEmail', email)
                    ctx.commit('ui/setStep', 'end', {root: true})
                },
                errorCallback: (errorRes) => {
                    ctx.commit(
                        'ui/showErrors',
                        errorRes.data.error.details,
                        {root: true}
                    )
                }
            })
        },
        endResetPasswordFlow (ctx, { email, code, newPassword1, newPassword2 }) {
            const data = new FormData();

            data.append('email', email);
            data.append('code', code);
            data.append('new_password1', newPassword1);
            data.append('new_password2', newPassword2);

            userService.endResetPasswordFlow(data, {
                successCallback: () => {
                    window.location = '/login/';
                },
                errorCallback: (errorRes) => {
                    ctx.commit(
                        'ui/showErrors',
                        errorRes.data.error.details,
                        {root: true}
                    )
                }
            })
        }
    }
})

export default store;