import { cartService } from '@/services'
import { createNamespacedTypes } from '@/utils/store'


const mutationTypes = {
	UPDATE_NAVIGATION_BAR_CART_INFO: 'UPDATE_NAVIGATION_BAR_CART_INFO'
}

const mutations = {
	[mutationTypes.UPDATE_NAVIGATION_BAR_CART_INFO] (_, payload) {
		const { totalPrice, productCount } = payload;

		const cartTotalPriceElm = document.getElementsByClassName('cart-total-price')[0];
		const cartProductCountElm = document.getElementById('cart-product-count');
	
		cartTotalPriceElm.innerHTML = totalPrice;
		cartProductCountElm.innerHTML = `(${productCount.toString()})`;
	}
}

const actionTypes = {
	BUY_NOW_PRODUCT: 'BUY_NOW_PRODUCT',
	ADD_PRODUCT_TO_CART: 'ADD_PRODUCT_TO_CART'
}

const actions = {
	[actionTypes.BUY_NOW_PRODUCT] (ctx, { productId }) {
		const data = new FormData()

		data.append('product_id', productId)

		cartService.addProduct(data, {
			successCallback: () => {
				window.location = '/cart/';
			}
		})
	},
	[actionTypes.ADD_PRODUCT_TO_CART] (ctx, { productId }) {
		const data = new FormData()

		data.append('product_id', productId)

		cartService.addProduct(data, {
			successCallback: ({ data }) => {
				const { product, cart } = data;

				const modalContext = { 
					product: {
						author: product.author, 
						title: product.title, 
						price: product.price,
						cover_img: {
							url: product.cover_img.path
						}
					}
				};

				this.$modalManager.show(
					'successCartUpdatedModal',
					modalContext
				);

				ctx.commit(
					mutationTypes.UPDATE_NAVIGATION_BAR_CART_INFO,
					{ 
						totalPrice: cart.total_price,
						productCount: cart.product_count
					},
					{ root: true }
				)
			}
		});
	}
}

export const cartModuleTypes = createNamespacedTypes('cart', {
	actions: actionTypes,
	mutations: mutationTypes
})

const cartModule = {
	actions,
	mutations,
	namespaced: true
}

export default cartModule;