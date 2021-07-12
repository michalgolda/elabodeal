import { createStore } from 'vuex';
import { uiModule } from './modules';

import userService from '@/services/user';


const initialState = () => {
	const { products } = window.__APP_CONTEXT__;

	return {
		products,
		selectedProducts: products
	}
};

const store = createStore({
	namespaced: true,
	state: initialState(),
	modules: {
		ui: uiModule
	},
	mutations: {
		removeProduct (state, product_id) {
			state.products = state.products.filter((product) => {
				return (product.id !== product_id);
			})
		},
		selectProduct (state, product_id) {
			const product = state.products.find((product) => {
				return (product.id === product_id);
			});

			state.selectedProducts.push(product);

			const cartTotalPriceElm = document.getElementsByClassName('cart-total-price')[1];

			const updatedTotalPrice = parseFloat(cartTotalPriceElm.innerText) + product.price;

			cartTotalPriceElm.innerText = updatedTotalPrice.toFixed(2).toString();
		},
		unSelectProduct (state, product_id) {
			const product = state.products.find((product) => {
				return (product.id === product_id);
			});

			state.selectedProducts = state.selectedProducts.filter((product) => {
				return (product.id !== product_id);
			});

			const cartTotalPriceElm = document.getElementsByClassName('cart-total-price')[1];

			const updatedTotalPrice = parseFloat(cartTotalPriceElm.innerText) - product.price;

			cartTotalPriceElm.innerText = updatedTotalPrice.toFixed(2).toString();
		}
	},
	actions: {
		saveCart (ctx, { title, description }) {
			const data = new FormData();

			data.append('title', title);
			data.append('description', description);

			userService.saveCart(data, {
				successCallback: () => {
					this.$modalManager.hide();
				},
				errorCallback: (errorRes) => {
					ctx.commit(
						'ui/setError',
						errorRes.data.error.details,
						{root: true}
					);
				}
			})
		},
		removeProductFromCart (ctx, { product_id }) {
			const data = new FormData();

			data.append('product_id', product_id);

			userService.removeProductFromCart({ data }, {
				successCallback: ({ data }) => {
					const { cart } = data;

					ctx.commit(
						'removeProduct',
						product_id
					);

					const cartTotalPriceElm = document.getElementsByClassName('cart-total-price');
					const cartProductCountElm = document.getElementById('cart-product-count');
				
					cartTotalPriceElm[0].innerHTML = cart.total_price;
					cartTotalPriceElm[1].innerHTML = cart.total_price;
					
					cartProductCountElm.innerHTML = `(${cart.product_count.toString()})`;
				}
			});
		}
	}
});

export default store;