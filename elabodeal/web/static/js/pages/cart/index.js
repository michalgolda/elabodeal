import { createApp } from 'vue';
import { mountPageComponents } from '@/utils/vue';
import createModalManager from '@/modalManager';
import storeAppGlobalPropertiesInjector from '@/utils/store';

import store from './store';

import ProductList from './components/ProductList';
import SaveCartBtn from './components/SaveCartBtn';
import SaveCartModal from './components/SaveCartModal';


const vueInstance = createApp();

const modalManager = createModalManager({
    modals: {
        saveCartModal: SaveCartModal
    }
});

vueInstance.use(modalManager);

const injectedStore = storeAppGlobalPropertiesInjector(
    store,
    ['$modalManager']
);

vueInstance.use(injectedStore);

mountPageComponents(vueInstance, {
    'product-list': ProductList,
    'save-cart-btn': SaveCartBtn
});