import { createStore } from 'vuex';
import { cartModule } from './modules';


const store = createStore({
	namespaced: true,
	modules: {
		cart: cartModule
	}
});

export default store;