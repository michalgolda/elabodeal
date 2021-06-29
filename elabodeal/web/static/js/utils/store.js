const storeAppGlobalPropertiesInjector = (store, properties) => {
	return {
		install (app, injectKey) {
			if (properties) {
				for (var propertyName of properties) {
					const appGlobalProperties = app.config.globalProperties;
					
					if (appGlobalProperties.hasOwnProperty(propertyName)) {
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

export default storeAppGlobalPropertiesInjector;