import { createStore } from "vuex";
import { appData } from '@/utils/data';
import {
	uiModule,
	userSettingsModule, 
	publisherSettingsModule } from "./modules";
 

const initialState = () => {
	const { user, publisher } = appData;

	return {
		user,
		publisher
	}
};

const store = createStore({
	namespaced: true,
	modules: {
		ui: uiModule,
		userSettings: userSettingsModule,
		publisherSettings: publisherSettingsModule
	},
	state: initialState(),
	mutations: {
		updateData (state, payload) {
			const { key, 
					fieldName, 
					fieldValue } = payload;

			state[key][fieldName] = fieldValue;
		}
	}
});

export default store;