import { createApp } from 'vue'
import { mountComponents } from '@/utils/vue'
import createModalManager from '@/modalManager'
import { globalPropertiesWrapper } from '@/utils/store'

import store from './store'

import ProductList from './components/ProductList'
import SaveCartBtn from './components/SaveCartBtn'
import SaveCartModal from './components/SaveCartModal'
import CreateCheckoutSessionBtn from './components/CreateCheckoutSessionBtn'


const app = createApp()

const modals = { saveCartModal: SaveCartModal }

const modalManager = createModalManager({ modals })

app.use(modalManager)

const wrappedStore = globalPropertiesWrapper(store, ['$modalManager'])

app.use(wrappedStore)

const components = {
    'product-list': ProductList,
    'save-cart-btn': SaveCartBtn,
    'create-checkout-session-btn': CreateCheckoutSessionBtn
}

mountComponents(app, components)