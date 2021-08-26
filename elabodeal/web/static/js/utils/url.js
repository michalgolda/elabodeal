/**
 * A function for setting a parameters of current url
 * 	
 * @param {String} paramKey 
 * @param {String} paramValue
 */
export function setCurrentURLParam (paramKey, paramValue) {
	const currentURL = new URL(window.location.href)
	const currentURLParams = currentURL.searchParams

	const actionType = paramValue ? 'SET' : 'DELETE'

	switch (actionType) {
		case 'SET':
			currentURLParams.set(
				paramKey,
				paramValue
			)

			break
		case 'DELETE':
			currentURLParams.delete(
				paramKey,
				paramValue
			)

			break
	}

	const updatedURLString = currentURL.toString()

	window.history.pushState(
		null, 
		null, 
		updatedURLString
	)
}

/**
 * A function for setting a many of parameters once 
 * 
 * @param {Object} params 
 */
export function setCurrentURLParams (params) {
	for (var paramKey in params) {
		const paramValue = params[paramKey]

		setCurrentURLParam(paramKey, paramValue)
	}
}

/**
 * A function which return a mapped current url parameters
 * 
 * @returns {Object}
 */
export function getCurrentURLParams () {
	const currentURLSearchParams = new URLSearchParams(window.location.search)

	const currentURLParams = Object.fromEntries(currentURLSearchParams)

	return currentURLParams
}

/**
 * A function which return a current url parameter value
 * 
 * @param {String} paramKey 
 * @return {String} 
 */
export function getCurrentURLParamValue (paramKey) {
	return getCurrentURLParams()[paramKey]
}