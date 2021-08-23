import { createApp } from 'vue'

import store from './store';

import Main from './components/Main'


const mountElement = document.getElementById('mount0_0')

const app = createApp(Main)

app.use(store);

app.mount(mountElement)