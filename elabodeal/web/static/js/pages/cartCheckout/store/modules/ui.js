const initialState = () => {
	const { step } = window.__APP_CONTEXT__['checkout_session'];

	return {
		currentStep: step ? step : 'deliver',
		error: {}
	}
};

const uiModule = {
	namespaced: true,
	state: initialState(),
	mutations: {
		setError(state, error) {
			state.error = error;
		},
		clearError(state) {
			state.error = {};
		},
		setCurrentStep(state, step) {
			state.currentStep = step;
		}
	}
};

export default uiModule;