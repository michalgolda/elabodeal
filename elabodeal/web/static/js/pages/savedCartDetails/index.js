import { createApp } from 'vue'
import { mountComponents } from '@/utils/vue'
import createModalManager from '@/modalManager'
import { globalPropertiesWrapper } from '@/utils/store'

import store from './store'

import ShareCartBtn from './components/ShareCartBtn'
import DeleteCartBtn from './components/DeleteCartBtn'
import SharedCartModal from './components/SharedCartModal'


const app = createApp()

const modals = { sharedCartModal: SharedCartModal }

const modalManager = createModalManager({ modals })

app.use(modalManager)

const wrappedStore = globalPropertiesWrapper(store, ['$modalManager'])

app.use(wrappedStore)

const components = {
    'share-cart-btn': ShareCartBtn,
    'delete-cart-btn': DeleteCartBtn 
}

mountComponents(app, components)