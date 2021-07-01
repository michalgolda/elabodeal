import userService from '@/services/user';


const userSettingsModule = {
	namespaced: true,
	actions: {
		changeUsername (ctx, { username }) {
			const data = new FormData();

			data.append('username', username);

			userService.updateSettings(data, {
				successCallback: () => {
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
						'ui/hideSection',
						null,
						{root: true}
					);
				},
				errorCallback: (errorRes) => {
					ctx.commit(
						'ui/setSectionError',
						errorRes.data.error.details,
						{root: true}
					);
				}
			});
		},
		changeEmail (ctx, { email }) {
			const data = new FormData();

			data.append('email', email);

			userService.changeEmail(data, {
				successCallback: () => {
					this.$modalManager.show('confirmEmailChangeModal', {
						email
					});

					ctx.commit(
						'ui/hideSection', 
						null, 
						{root:true}
					);
				},
				errorCallback: (errorRes) => {
					ctx.commit(
						'ui/setSectionError',
						errorRes.data.error.details,
						{root: true}
					);
				}
			});
		},
		resendChangeEmailCode (ctx, { email }) {
			const data = new FormData();

			data.append('email', email);

			userService.changeEmail(data);
		},
		confirmChangeEmail (ctx, { email, code }) {
			const data = new FormData();

			data.append('code', code);
			data.append('email', email);

			userService.confirmEmailChange(data, {
				successCallback: () => {
					this.$modalManager.hide();

					ctx.commit(
						'updateData',
						{
							key: 'user',
							fieldName: 'email',
							fieldValue: email
						},
						{root: true}
					);
				},
				errorCallback: (errorRes) => {
					ctx.commit(
						'ui/setSectionError',
						errorRes.data.error.details,
						{root: true}
					);
				}
			});
		},
		changePassword (ctx, { currentPassword, newPassword }) {
			const data = new FormData();

			data.append('new_password', newPassword);
			data.append('current_password', currentPassword);
	
			userService.changePassword(data, {
				successCallback: () => {
					ctx.commit(
						'ui/hideSection',
						null,
						{root: true}
					);
				},
				errorCallback: (errorRes) => {
					ctx.commit(
						'ui/setSectionError',
						errorRes.data.error.details,
						{root: true}
					);
				}
			});
		},
		toggleNewsletter (ctx, { value }) {
			const data = new FormData();

			data.append('newsletter', value);

			userService.updateSettings(data, {
				hideDefaultSuccessMsg: true,
				hideDefaultErrorMsg: true
			});
		}
	}
};

export default userSettingsModule;