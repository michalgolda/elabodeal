import { createApp } from 'vue'
import { mountComponents } from '@/utils/vue'

import store from './store'

import LanguagesChart from './components/LanguagesChart'
import CategoriesChart from './components/CategoriesChart'
import ProfileBadgeBtn from './components/ProfileBadgeBtn'


const app = createApp()

app.use(store)

const components = {
    'followBtn': ProfileBadgeBtn,
    'unFollowBtn': ProfileBadgeBtn,
    'languagesChart': LanguagesChart,
    'categoriesChart': CategoriesChart
}

mountComponents(app, components)