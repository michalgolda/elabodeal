function loadAppData (appDataElementId = 'app-data') {
	const appDataElement = document.getElementById(appDataElementId);
	const appData = JSON.parse(appDataElement.textContent);

	return appData;
}

export const appData = loadAppData();