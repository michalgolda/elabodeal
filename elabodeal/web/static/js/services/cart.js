import Service from '@/services/base';


const cartService = new Service('cart');

cartService.registerFunction('addProduct', {
	url: '/api/cart/',
	method: 'post'
});


cartService.registerFunction('removeProduct', {
	url: '/api/cart/',
	method: 'delete',
	successMsg: 'Produkt został pomyślnie usunięty z koszyka.'
});


cartService.registerFunction('selectOrDeselectProduct', {
	url: '/api/cart/',
	method: 'put'
});


cartService.registerFunction('save', {
	url: '/api/me/carts/',
	method: 'post',
	successMsg: 'Koszyk został pomyślnie zapisany.'
});


export default cartService;