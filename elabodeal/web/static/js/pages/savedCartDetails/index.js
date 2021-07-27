import { createApp } from 'vue';
import storeAppGlobalPropertiesInjector from '@/utils/store';
import { mountPageComponents } from '@/utils/vue';
import createModalManager from '@/modalManager';

import store from './store';

import DeleteCartBtn from './components/DeleteCartBtn';
import ShareCartBtn from './components/ShareCartBtn';
import SharedCartModal from './components/SharedCartModal';


const vueInstance = createApp();

const modalManager = createModalManager({
    modals: {
        sharedCartModal: SharedCartModal
    }
});

vueInstance.use(modalManager);

const injectedStore = storeAppGlobalPropertiesInjector(
	store, 
	['$modalManager']
);

vueInstance.use(injectedStore);


mountPageComponents(vueInstance, {
    'share-cart-btn': ShareCartBtn,
    'delete-cart-btn': DeleteCartBtn
});