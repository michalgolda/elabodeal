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

publisherService.registerFunction('follow', {
	url: '/api/followers/',
	method: 'post'
});

publisherService.registerFunction('unfollow', {
	url: '/api/followers/',
	method: 'delete'
});

publisherService.registerFunction('updateProfile', {
	url: '/api/profile/',
	method: 'put',
	successMsg: 'Profil został pomyślnie zaktualizowany.'
})

publisherService.registerFunction('updateProfileBannerImg', {
	url: '/api/profile/banner_img/',
	method: 'put'
})

publisherService.registerFunction('updateProfileAvatarImg', {
	url: '/api/profile/avatar_img/',
	method: 'put'
})

export default publisherService;