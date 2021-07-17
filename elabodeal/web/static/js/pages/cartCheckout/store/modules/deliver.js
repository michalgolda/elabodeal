import cartService from '@/services/cart';


const initialState = () => {
	const { delivery } = window.__APP_CONTEXT__['checkout_session'];

	return {
		delivery: delivery ? delivery : {},
		collectedDeliverData: delivery ? true : false
	}
};


const deliverModule = {
	namespaced: true,
	state: initialState(),
	mutations: {
		toggleCollectedDeliverData (state) {
			const collectDeliverData = state.collectDeliverData;
			const deliverDataIsCollected = collectDeliverData ? false : true;

			state.collectedDeliverData = deliverDataIsCollected;
		},
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
		
			cartService.updateCheckoutSession(data, {
				successCallback: ({ data }) => {
					ctx.commit('toggleCollectedDeliverData');
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