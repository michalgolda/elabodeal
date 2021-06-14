export const setCurrentUrlParam = (paramKey, paramValue) => {
	const currentURL = new URL(window.location.href);
	const currentURLParams = currentURL.searchParams;
	
	const actionType = paramValue ? 'SET' : 'DELETE';

	switch (actionType) {
		case 'SET':
			currentURLParams.set(paramKey, paramValue);

			break;
		case 'DELETE':
			currentURLParams.delete(paramKey, paramValue);

			break;
	}

	const newURLString = currentURL.toString();

	window.history.pushState(null, null, newURLString);
};

export const setCurrentUrlParams = (params) => {
	const paramKeys = Object.keys(params);

	for (var paramKey of paramKeys) {
		const paramValue = params[paramKey];

		setCurrentUrlParam(paramKey, paramValue);
	}
};