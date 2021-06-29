import { createApp, h as createElement } from 'vue';
import storeAppGlobalPropertiesInjector from '@/utils/store';
import createModalManager from '@/modalManager';
import store from './store';

import Main from './components/Main';
import ConfirmEmailChangeModal from './components/ConfirmEmailChangeModal';


const mountElement = document.getElementById('mount0_0');

const vueInstance = createApp({
	render() {
		return createElement(Main);
	}
});

const modalManager = createModalManager({
	modals: {
		confirmEmailChangeModal: ConfirmEmailChangeModal
	}
});

vueInstance.use(modalManager);

const injectedStore = storeAppGlobalPropertiesInjector(store, ['$modalManager']);

vueInstance.use(injectedStore);

vueInstance.mount(mountElement);