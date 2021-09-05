import { createApp } from 'vue'
import { mountComponents } from '@/utils/vue'
import createModalManager from '@/modalManager'
import { globalPropertiesWrapper } from '@/utils/store'

import store from './store'

import EditBtn from './components/EditBtn'
import EditModal from './components/EditModal'
import LanguagesChart from './components/LanguagesChart'
import CategoriesChart from './components/CategoriesChart'
import FollowersBtnWrapper from './components/FollowersBtnWrapper'


const app = createApp()


const modals = { editModal: EditModal }

const modalManager = createModalManager({ modals })

app.use(modalManager)


const wrappedStore = globalPropertiesWrapper(store, ['$modalManager'])

app.use(wrappedStore)


const components = {
    'editBtn': EditBtn,
    'languagesChart': LanguagesChart,
    'categoriesChart': CategoriesChart,
    'followBtn': FollowersBtnWrapper,
    'unFollowBtn': FollowersBtnWrapper
}

mountComponents(app, components)