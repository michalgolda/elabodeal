import { setCurrentUrlParam } from '@/utils/url'


const initialState = () => {
    return {
        step: 'start',
        errors: {}
    }
}

const uiModule = {
    namespaced: true,
    state: initialState(),
    mutations: {
        setStep (state, step) {
            step = step ? step.toLowerCase() : 'start';

            setCurrentUrlParam('step', step);

            state.step = step;
        },
        showErrors (state, errors) {
            state.errors = errors;
        }
    }
}

export default uiModule;