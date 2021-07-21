import { createStore } from 'vuex';
import { appData } from '@/utils/data';
import { checkoutSessionService } from '@/services';

import { uiModule, deliverModule, paymentModule } from './modules';


const initialState = () => {
	const { 
		user, 
		checkout_session: checkoutSession } = appData;

	const delivery = checkoutSession['delivery'] ? checkoutSession['delivery'] : {};

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
			checkoutSessionService.removeSession(null, {
				successCallback: () => {
					window.location = '/c/';
				}
			});
		}
	}
});

export default store;