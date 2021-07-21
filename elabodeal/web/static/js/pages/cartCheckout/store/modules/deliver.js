import { appData } from '@/utils/data';
import { checkoutSessionService } from '@/services';


const initialState = () => {
	const { delivery } = appData;

	return {
		delivery: delivery ? delivery : {}
	}
};


const deliverModule = {
	namespaced: true,
	state: initialState(),
	mutations: {
		setDeliveryData (state, data) {
			state.delivery = data;
		} 
	},
	actions: {
		collectDeliverData (ctx, { first_name, last_name, email }) {
			const data = new FormData();

			data.append('email', email);
			data.append('last_name', last_name);
			data.append('first_name', first_name);
		
			checkoutSessionService.updateSession(data, {
				successCallback: ({ data }) => {
					ctx.commit('setDeliveryData', data.delivery);
					ctx.commit('ui/setCurrentStep', 'payment', {root: true});
				},
				errorCallback: (errorRes) => {
					ctx.commit(
						'ui/setError',
						errorRes.data.error.details,
						{root:true}
					);
				}
			});
		}
	}
};


export default deliverModule;