import { createStore } from 'vuex';
import { cartModule } from './modules';
import { cartService } from '@/services';


const store = createStore({
	namespaced: true,
	modules: {
		cart: cartModule
	},
	actions: {
		buyNowProduct (ctx, { productId }) {
			const data = new FormData();

			data.append('product_id', productId);

			cartService.addProduct(data, {
				successCallback: () => {
					window.location = '/c/';
				}
			});
		}
	}
});

export default store;