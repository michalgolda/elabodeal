import userService from '@/services/user';


const cartModule = {
	namespaced: true,
	actions: {
		addProductToCart (ctx, { productId }) {
			const data = new FormData();

			data.append('product_id', productId);

			userService.addProductToCart(data, {
				successCallback: ({ data }) => {
					const { author, title, price, cover_img } = data;

					const modalContext = { 
						product: {
							author, 
							title, 
							price,
							cover_img: {
								url: cover_img.path
							}
						}
					};

					this.$modalManager.show(
						'successCartUpdatedModal',
						modalContext
					);
				}
			});
		}
	}
};


export default cartModule;