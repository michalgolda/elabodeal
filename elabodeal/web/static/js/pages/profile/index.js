import { createApp } from 'vue'
import { mountComponents } from '@/utils/vue'

import store from './store'

import LanguagesChart from './components/LanguagesChart'
import CategoriesChart from './components/CategoriesChart'
import FollowersBtnWrapper from './components/FollowersBtnWrapper'


const app = createApp()

app.use(store)

const components = {
    'languagesChart': LanguagesChart,
    'followBtn': FollowersBtnWrapper,
    'categoriesChart': CategoriesChart,
    'unFollowBtn': FollowersBtnWrapper
}

mountComponents(app, components)