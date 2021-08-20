import { createApp } from 'vue';
import { mountPageComponents } from '@/utils/vue';

import store from './store';

import LanguagesChart from './components/LanguagesChart';
import CategoriesChart from './components/CategoriesChart';
import ProfileBadgeBtn from './components/ProfileBadgeBtn';


const app = createApp();

app.use(store);

mountPageComponents(app, {
    'followBtn': ProfileBadgeBtn,
    'unFollowBtn': ProfileBadgeBtn,
    'languagesChart': LanguagesChart,
    'categoriesChart': CategoriesChart
});