import { createApp } from 'vue';
import createModalManager from '@/modalManager';
import { mountPageComponents } from '@/utils/vue';
import storeAppGlobalPropertiesInjector from '@/utils/store';

import store from './store';

import TextDetails from './components/TextDetails';
import AddToCartBtn from './components/AddToCartBtn';
import SuccessCartUpdatedModal from './components/SuccessCartUpdatedModal';


const vueInstance = createApp();

const modalManager = createModalManager({
	modals: {
		successCartUpdatedModal: SuccessCartUpdatedModal
	}
});

vueInstance.use(modalManager);

const injectedStore = storeAppGlobalPropertiesInjector(
	store, 
	['$modalManager']
);

vueInstance.use(injectedStore);


mountPageComponents(vueInstance, {
	'text-details': TextDetails,
	'add-to-cart': AddToCartBtn
});