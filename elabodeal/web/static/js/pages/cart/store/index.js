import { createStore } from 'vuex';
import { uiModule } from './modules';
import { appData } from '@/utils/data';

import cartService from '@/services/cart';


const initialState = () => {
	const { products } = appData;

	return {
		products,
		selectedProducts: products.filter((product) => {
			return (product.selected === true);
		})
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
		deselectProduct (state, product_id) {
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

			cartService.save(data, {
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

			cartService.removeProduct({ data }, {
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
					
					cartProductCountElm.innerHTML = `(${cart.product_count})`;

					document.title = `Elabodeal - Koszyk (${cart.product_count})`;
				}
			});
		},
		selectOrDeselectProduct (ctx, { product_id, selected }) {
			const data = new FormData();

			data.append('product_id', product_id);

			cartService.selectOrDeselectProduct(data, {
				successCallback: () => {
					const actionType = selected ? 'SELECT' : 'UNSELECT';

					switch (actionType) {
						case 'SELECT':
							ctx.commit('selectProduct', product_id);

							break;
						case 'UNSELECT':
							ctx.commit('deselectProduct', product_id);

							break;
					}
				}
			});
		},
		createCheckoutSession () {
			cartService.createCheckoutSession(null, {
				successCallback: () => {
					window.location = '/c/checkout/';
				}
			});
		}
	}
});

export default store;