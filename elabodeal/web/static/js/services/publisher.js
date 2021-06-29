import Service from "@/services";


const publisherService = new Service('publisher');

publisherService.register_function('createProduct', {
	url: '/api/me/products/',
	method: 'post',
	successMsg: 'Produkt został pomyślnie dodany.',
	errorMsg: 'Popraw błędy w formularzu'

});

publisherService.register_function('updateSettings', {
	url: '/api/me/settings/publisher/',
	method: 'put',
	successMsg: 'Ustawienia zostały pomyślnie zapisane.',
	errorMsg: 'Wprowadzone dane są nieprawidłowe. Spróbuj ponownie.'
});

export default publisherService;