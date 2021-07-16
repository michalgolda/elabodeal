import Service from '@/services';


const cartService = new Service('cart');

cartService.register_function('addProduct', {
	url: '/api/cart/',
	method: 'put'
});


cartService.register_function('removeProduct', {
	url: '/api/cart/',
	method: 'delete',
	successMsg: 'Produkt został pomyślnie usunięty z koszyka.'
});


cartService.register_function('save', {
	url: '/api/cart/save/',
	method: 'post',
	successMsg: 'Koszyk został pomyślnie zapisany.'
});


cartService.register_function('createCheckoutSession', {
	url: '/api/cart/checkout/session/',
	method: 'post'
});


cartService.register_function('updateCheckoutSession', {
	url: '/api/cart/checkout/session/',
	method: 'put'
});


cartService.register_function('removeCheckoutSession', {
	url: '/api/cart/checkout/session/',
	method: 'delete'
});


export default cartService;