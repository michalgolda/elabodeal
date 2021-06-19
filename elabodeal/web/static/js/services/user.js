import Service from '@/services';


const userService = new Service('user');

userService.register_function('updateSettings', {
	url: '/api/me/settings/',
	method: 'put',
	successMsg: 'Ustawienia zostały poprawnie zapisane.',
	errorMsg: 'Wprowadzone dane są nieprawidłowe. Spórbuj ponwonie.'
});


userService.register_function('changeEmail', {
	url: '/api/me/settings/email/',
	method: 'post',
	errorMsg: 'Wprowadzony email jest zajęty.'
});


userService.register_function('confirmEmailChange', {
	url: '/api/me/settings/email/confirm/',
	method: 'post',
	successMsg: 'Adres email został pomyślnie zmieniony.',
	errorMsg: 'Wprowadzony kod jest niepoprwany.'
});

export default userService;