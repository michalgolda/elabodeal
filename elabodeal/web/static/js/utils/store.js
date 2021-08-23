const storeAppGlobalPropertiesInjector = (store, properties) => {
	return {
		install (app, injectKey) {
			if (properties) {
				for (var propertyName of properties) {
					const appGlobalProperties = app.config.globalProperties;
					
					if (appGlobalProperties[propertyName] !== undefined) {
						store[propertyName] = appGlobalProperties[propertyName];
					} else {
						console.warn(`You are want inject property to store which aren't exists.`);
					}

				}
			}

			store.install(app, injectKey);
		}
	}
};

export const createNamespacedTypes = (namespace, definitions) => {
	for (var definitionName in definitions) {
		const types = definitions[definitionName]
		
		for (var typeName in types)
			types[typeName] = `${namespace}/${typeName}`
	}

	return definitions
}

export default storeAppGlobalPropertiesInjector;