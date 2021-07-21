import Service from '@/services/base';


const checkoutSessionService = new Service('checkoutSessionService');


checkoutSessionService.register_function('createSession', {
	url: '/api/checkout_session/',
	method: 'post'
});


checkoutSessionService.register_function('updateSession', {
	url: '/api/checkout_session/',
	method: 'put'
});


checkoutSessionService.register_function('removeSession', {
	url: '/api/checkout_session/',
	method: 'delete'
});


checkoutSessionService.register_function('succeedSession', {
	url: '/api/checkout_session/succeed/',
	method: 'post'
});


export default checkoutSessionService;