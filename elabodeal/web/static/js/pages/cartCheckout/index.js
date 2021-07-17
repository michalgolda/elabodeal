import { createApp } from 'vue';
import store from './store';

import Main from './components/Main';


const vueInstance = createApp(Main);

const mountElement = document.getElementById('mount0_0');

vueInstance.use(store);

vueInstance.mount(mountElement);