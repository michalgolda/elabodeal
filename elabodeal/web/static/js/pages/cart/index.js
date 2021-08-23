import { createApp } from 'vue';
import { mountPageComponents } from '@/utils/vue';
import createModalManager from '@/modalManager';
import storeAppGlobalPropertiesInjector from '@/utils/store';

import store from './store';

import ProductList from './components/ProductList';
import SaveCartBtn from './components/SaveCartBtn';
import SaveCartModal from './components/SaveCartModal';
import CreateCheckoutSessionBtn from './components/CreateCheckoutSessionBtn';


const app = createApp();

const modalManager = createModalManager({
    modals: {
        saveCartModal: SaveCartModal
    }
});

app.use(modalManager);

const injectedStore = storeAppGlobalPropertiesInjector(
    store,
    ['$modalManager']
);

app.use(injectedStore);

mountPageComponents(app, {
    'product-list': ProductList,
    'save-cart-btn': SaveCartBtn,
    'create-checkout-session-btn': CreateCheckoutSessionBtn
});