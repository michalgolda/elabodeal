import Service from '@/services';


const userService = new Service('user');

userService.register_function('updateSettings', {
	url: '/api/me/settings/',
	method: 'put',
	successMsg: 'Ustawienia zostały poprawnie zapisane.'
});


userService.register_function('changeEmail', {
	url: '/api/me/settings/email/',
	method: 'post',
	successMsg: 'Kod weryfikacyjny został wysłany na podany adres email.',
	errorMsg: 'Wprowadzony email jest zajęty lub błędny.'
});


userService.register_function('confirmEmailChange', {
	url: '/api/me/settings/email/confirm/',
	method: 'post',
	successMsg: 'Adres email został pomyślnie zmieniony.',
	errorMsg: 'Wprowadzony kod jest niepoprwany.'
});


userService.register_function('changePassword', {
	url: '/api/me/settings/password/',
	method: 'put',
	successMsg: 'Hasło zostało pomyślnie zmienione.'
});


export default userService;