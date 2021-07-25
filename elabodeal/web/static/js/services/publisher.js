import Service from '@/services/base';


const publisherService = new Service('publisher');

publisherService.registerFunction('createProduct', {
	url: '/api/me/products/',
	method: 'post',
	successMsg: 'Produkt został pomyślnie dodany.',
	errorMsg: 'Popraw błędy w formularzu'
});

publisherService.registerFunction('updateSettings', {
	url: '/api/me/settings/publisher/',
	method: 'put',
	successMsg: 'Ustawienia zostały pomyślnie zapisane.'
});

export default publisherService;