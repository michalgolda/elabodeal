import { createStore } from 'vuex';
import { userService } from '@/services';
import { getCurrentURLParamValue } from '@/utils/url';


const initialState = () => {
    const email = getCurrentURLParamValue('email');
    const code = getCurrentURLParamValue('code');
    
    return {
        email,
        code,
        error: {}
    }
};

const store = createStore({
    state: initialState(),
    mutations: {
        setError (state, error) {
            state.error = error;
        }
    },
    actions: {
        registerConfirmation (ctx, { email, code }) {
            const data = new FormData();

            data.append('code', code);
            data.append('email', email);
        
            userService.registerConfirmation(data, {
                successCallback: () => {
                    window.location = '/login/';
                },
                errorCallback: (errorRes) => {
                    ctx.commit(
                        'setError',
                        errorRes.data.error.details
                    );
                }
            });
        },
        resendRegisterConfirmation (ctx, { email }) {
            const data = new FormData();

            data.append('email', email);

            userService.resendRegisterConfirmation(data);
        }
    }
})

export default store;