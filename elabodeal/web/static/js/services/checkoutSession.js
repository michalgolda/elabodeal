import Service from '@/services/base';


const checkoutSessionService = new Service('checkoutSessionService');


checkoutSessionService.registerFunction('createSession', {
	url: '/api/checkout_session/',
	method: 'post'
});


checkoutSessionService.registerFunction('updateSession', {
	url: '/api/checkout_session/',
	method: 'put'
});


checkoutSessionService.registerFunction('removeSession', {
	url: '/api/checkout_session/',
	method: 'delete'
});


checkoutSessionService.registerFunction('succeedSession', {
	url: '/api/checkout_session/succeed/',
	method: 'post'
});


export default checkoutSessionService;