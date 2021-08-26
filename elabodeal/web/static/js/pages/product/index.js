import { createApp } from 'vue'
import { mountComponents } from '@/utils/vue'
import createModalManager from '@/modalManager'
import { globalPropertiesWrapper } from '@/utils/store'

import store from './store'

import BuyNowBtn from './components/BuyNowBtn'
import TextDetails from './components/TextDetails'
import AddToCartBtn from './components/AddToCartBtn'
import SuccessCartUpdatedModal from './components/SuccessCartUpdatedModal'


const app = createApp()

const modals = { successCartUpdatedModal: SuccessCartUpdatedModal }

const modalManager = createModalManager({ modals })

app.use(modalManager)

const wrappedStore = globalPropertiesWrapper(store, ['$modalManager'])

app.use(wrappedStore);

const components = {
	'buy-now': BuyNowBtn,
	'text-details': TextDetails,
	'add-to-cart': AddToCartBtn
}

mountComponents(app, components)