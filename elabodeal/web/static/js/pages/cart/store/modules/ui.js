const initialState = () => {
	return {
		error: {}
	}
};

const uiModule = {
	namespaced: true,
	state: initialState(),
	mutations: {
		setError (state, error) {
			state.error = error;
		},
		clearError (state) {
			state.error = {};
		}
	}
}

export default uiModule;