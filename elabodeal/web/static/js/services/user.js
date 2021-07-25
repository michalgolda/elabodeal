import Service from '@/services/base';


const userService = new Service('user');

userService.registerFunction('updateSettings', {
	url: '/api/me/settings/',
	method: 'put',
	successMsg: 'Ustawienia zostały poprawnie zapisane.'
});


userService.registerFunction('changeEmail', {
	url: '/api/me/settings/email/',
	method: 'post',
	successMsg: 'Kod weryfikacyjny został wysłany na podany adres email.',
	errorMsg: 'Wprowadzony email jest zajęty lub błędny.'
});


userService.registerFunction('confirmEmailChange', {
	url: '/api/me/settings/email/confirm/',
	method: 'post',
	successMsg: 'Adres email został pomyślnie zmieniony.',
	errorMsg: 'Wprowadzony kod jest niepoprwany.'
});


userService.registerFunction('changePassword', {
	url: '/api/me/settings/password/',
	method: 'put',
	successMsg: 'Hasło zostało pomyślnie zmienione.'
});


export default userService;