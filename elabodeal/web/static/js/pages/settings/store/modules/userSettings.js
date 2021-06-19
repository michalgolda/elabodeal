import userService from '@/services/user';


const userSettingsModule = {
	namespaced: true,
	actions: {
		changeUsername(ctx, username) {
			const data = new FormData();

			data.append('username', username);

			userService.updateSettings(data, 
				() => {
					const navUsernameElm = document.getElementsByClassName('nav__username')[0];

					navUsernameElm.textContent = username;

					ctx.commit(
						'updateData',
						{
							key: 'user',
							fieldName: 'username',
							fieldValue: username
						},
						{root: true}
					);

					ctx.commit(
						'ui/setCurrentSection',
						null,
						{root: true}
					);
				},
				() => {
					ctx.commit(
						'ui/setCurrentSectionError',
						true,
						{root: true}
					);
				}
			);
		},
		changeEmail(ctx, email) {
			const data = new FormData();

			data.append('email', value);

			userService.changeEmail(data,
				() => {
					
				},
				() => {

				}
			);
		},
		confirmChangeEmail(ctx, email, code) {
			const data = new FormData();

			data.append('code', code);
			data.append('email', email);

			userService.confirmEmailChange(data,
				() => {

				},
				() => {
					
				}
			);
		}
	}
};

export default userSettingsModule;