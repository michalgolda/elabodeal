import publisherService from '@/services/publisher';


const publisherSettingsModule = {
	namespaced: true,
	actions: {
		changeFirstName (ctx, { first_name }) {
			const data = new FormData();

			data.append('first_name', first_name);

			publisherService.updateSettings(data, {
				successCallback: () => {
					ctx.commit(
						'updateData',
						{
							key: 'publisher',
							fieldName: 'first_name',
							fieldValue: first_name
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
		changeLastName (ctx, { last_name }) {
			const data = new FormData();

			data.append('last_name', last_name);

			publisherService.updateSettings(data, {
				successCallback: () => {
					ctx.commit(
						'updateData',
						{
							key: 'publisher',
							fieldName: 'last_name',
							fieldValue: last_name
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
		changeSwift (ctx, { swift }) {
			const data = new FormData();

			data.append('swift', swift);

			publisherService.updateSettings(data, {
				successCallback: () => {
					ctx.commit(
						'updateData',						{
							key: 'publisher',
							fieldName: 'swift',
							fieldValue: swift
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
		changeAccountNumber (ctx, { account_number }) {
			const data = new FormData();

			data.append('account_number', account_number);

			publisherService.updateSettings(data, {
				successCallback: () => {
					ctx.commit(
						'updateData',						{
							key: 'publisher',
							fieldName: 'account_number',
							fieldValue: account_number
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
		}
	}
};

export default publisherSettingsModule;