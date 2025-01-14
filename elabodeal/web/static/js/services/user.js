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


userService.registerFunction('createPublisher', {
	url: '/api/publisher_application/',
	method: 'post'
});


userService.registerFunction('registerConfirmation', {
	url: '/api/confirm/',
	method: 'post'
});


userService.registerFunction('resendRegisterConfirmation', {
	url: '/api/confirm/resend/',
	method: 'post',
	successMsg: 'Nowy kod aktywacyjny został wysłany.'
});


userService.registerFunction('startResetPasswordFlow', {
	url: '/api/reset-password/',
	method: 'post',
	successMsg: 'Na podany adres email został wysłany kod bezpieczeństwa.'
});


userService.registerFunction('endResetPasswordFlow', {
	url: '/api/reset-password/',
	method: 'put',
	successMsg: 'Hasło zostało pomyślnie zresetowane.'
});

export default userService;