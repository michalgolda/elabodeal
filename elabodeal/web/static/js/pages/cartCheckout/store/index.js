import { createStore } from 'vuex';
import cartService from '@/services/cart';

import { uiModule, deliverModule, paymentModule } from './modules';


const initialState = () => {
	const { user, checkout_session } = window.__APP_CONTEXT__;
	const delivery = checkout_session.delivery ? checkout_session.delivery : {};

	return { 
		first_name: delivery.first_name, 
		last_name: delivery.last_name, 
		email: delivery.email ? delivery.email : user.email };
};


const store = createStore({
	namespaced: true,
	modules: {
		ui: uiModule,
		deliver: deliverModule,
		payment: paymentModule
	},
	state: initialState,
	actions: {
		cancelCheckoutProcess (	) {
			cartService.removeCheckoutSession(null, {
				successCallback: () => {
					window.location = '/c/';
				}
			});
		}
	}
});

export default store;