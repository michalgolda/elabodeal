/**
 * A function which get data 
 * from script element which contain a data.
 * 
 * @param {String} dataElementId
 * @return {Object}
 */
export function getApplicationData (dataElementId = 'application-data') {
	const dataElm = document.getElementById(dataElementId)

	!dataElm && console.error(
		`
		You are try to get application 
		data from element which doesn't exists
		`
	)
	
	const stringData = dataElm.textContent

	const parsedData = JSON.parse(stringData)

	return parsedData
}