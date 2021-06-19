import { setCurrentUrlParams } from '@/utils/url';


const initialState = () => {
	return {
		currentTab: 'user',
		currentSection: '',
		currentSectionError: null
	}
}

const uiModule = {
	namespaced: true,
	state: initialState(),
	mutations: {
		setCurrentTab(state, tabName) {
			tabName = tabName ? tabName.toLowerCase() : 'user';

			setCurrentUrlParams({
				tab: tabName,
				section: null
			});

			state.currentTab = tabName;
		},
		setCurrentSection(state, sectionName) {
			sectionName = sectionName ? sectionName.toLowerCase() : '';

			setCurrentUrlParams({
				section: sectionName
			});

			state.currentSection = sectionName;
		},
		setCurrentSectionError(state, error) {
			state.currentSectionError = error;
		}
	}
};

export default uiModule;