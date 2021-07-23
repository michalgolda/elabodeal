import { createStore } from 'vuex';
import { cartModule } from './modules';
import { cartService, checkoutSessionService } from '@/services';


const store = createStore({
	namespaced: true,
	modules: {
		cart: cartModule
	},
	actions: {
		buyNowProduct (ctx, { productId }) {
			const data = new FormData();

			data.append('clear', true);
			data.append('product_id', productId);

			cartService.addProduct(data, {
				successCallback: () => {
					checkoutSessionService.createSession(null, {
						successCallback: () => {
							window.location = '/c/checkout/';
						}
					});
				}
			});
		}
	}
});

export default store;