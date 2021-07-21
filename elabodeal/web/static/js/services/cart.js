import Service from '@/services/base';


const cartService = new Service('cart');

cartService.register_function('addProduct', {
	url: '/api/cart/',
	method: 'post'
});


cartService.register_function('removeProduct', {
	url: '/api/cart/',
	method: 'delete',
	successMsg: 'Produkt został pomyślnie usunięty z koszyka.'
});


cartService.register_function('selectOrDeselectProduct', {
	url: '/api/cart/',
	method: 'put'
});


cartService.register_function('save', {
	url: '/api/cart/save/',
	method: 'post',
	successMsg: 'Koszyk został pomyślnie zapisany.'
});


export default cartService;