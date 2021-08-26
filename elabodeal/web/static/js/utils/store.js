/**
 * A function which get passed vue app global properties 
 * names as arguments and inject its to vuex store object.
 * 
 * @param {VuexStore} store 
 * @param {Array} properties 
 * @return {Object}
 */
export function globalPropertiesWrapper (store, properties) {
	const install = (app) => {
		if (properties) {
			for (var propertyName of properties) {
				const globalProperties = app.config.globalProperties
	
				if (globalProperties.hasOwnProperty(propertyName)) {
					store[propertyName] = globalProperties[propertyName]
				} else {
					console.warn(
						`
						You are want inject property 
						to store which aren't exists.
						`
					)
				}
			}
		}

		store.install(app)
	}

	return { install }
}

/**
 * A function create namespaced 
 * vuex types of mutations, actions etc.
 * 
 * @param {String} namespace
 * @param {Object} typesDefinition
 * @return {Object}
 */
export function createNamespacedTypes (namespace, typesDefinition) {
	// This way of clone object must be a replaced in the future with loadash
	const typesDefinitionCopy = JSON.parse(JSON.stringify(typesDefinition))

	for (var typeDefinitionName in typesDefinitionCopy) {
		const types = typesDefinitionCopy[typeDefinitionName]

		for (var typeName in types)
			types[typeName] = `${namespace}/${typeName}`
	}
	
	return typesDefinitionCopy
}