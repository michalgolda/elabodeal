import { setCurrentUrlParam } from '@/utils/url';


const initialState = () => {
    const urlSearchParams = new URLSearchParams(window.location.search);

    const formType = urlSearchParams.get('formType');

    return {
        errors: {},
        formType: formType === 'invidual' ? 'invidual' : null
    }
};

const uiModule = {
    namespaced: true,
    state: initialState(),
    mutations: {
        setFormType (state, formType) {
            setCurrentUrlParam('formType', formType);

            state.formType = formType;
        },
        setErrors (state, errors) {
            state.errors = errors;
        }
    }
};

export default uiModule;