import { createApp } from 'vue'
import createModalManager from '@/modalManager'
import { globalPropertiesWrapper }  from '@/utils/store'

import store from './store';

import Main from './components/Main'
import ConfirmEmailChangeModal from './components/ConfirmEmailChangeModal'


const app = createApp(Main)

const modals = { confirmEmailChangeModal: ConfirmEmailChangeModal }

const modalManager = createModalManager({ modals })

app.use(modalManager)

const wrappedStore = globalPropertiesWrapper(store, ['$modalManager'])

app.use(wrappedStore)

const mountElement = document.getElementById('mount0_0')

app.mount(mountElement)