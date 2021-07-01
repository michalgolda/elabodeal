import { setCurrentUrlParams } from '@/utils/url';


const initialState = () => {
	return {
		tab: {
			name: 'user'
		},
		section: {
			name: '',
			error: {}
		}
	}
}

const uiModule = {
	namespaced: true,
	state: initialState(),
	mutations: {
		showTab(state, tabName) {
			tabName = tabName ? tabName.toLowerCase() : 'user';

			setCurrentUrlParams({
				tab: tabName,
				section: null
			});

			state.tab.name = tabName;
		},
		showSection(state, sectionName) {
			sectionName = sectionName ? sectionName.toLowerCase() : '';

			setCurrentUrlParams({
				section: sectionName
			});

			state.section.name = sectionName;
			state.section.error = {};
		},
		hideSection(state) {
			setCurrentUrlParams({
				section: ''
			});

			state.section.name = '';
			state.section.error = {};
		},	
		setSectionError(state, error) {
			state.section.error = error;
		},
		clearSectionError(state) {
			state.section.error = {};
		}
	},
	getters: {
		currentTabName: state => state.tab.name
	}
};

export default uiModule;