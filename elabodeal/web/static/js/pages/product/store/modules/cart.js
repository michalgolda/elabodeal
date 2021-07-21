import { cartService } from '@/services';


const cartModule = {
	namespaced: true,
	actions: {
		addProductToCart (ctx, { productId }) {
			const data = new FormData();

			data.append('product_id', productId);

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

					const cartTotalPriceElm = document.getElementsByClassName('cart-total-price')[0];
					const cartProductCountElm = document.getElementById('cart-product-count');
				
					cartTotalPriceElm.innerHTML = cart.total_price;
					cartProductCountElm.innerHTML = `(${cart.product_count.toString()})`;
				}
			});
		}
	}
};


export default cartModule;