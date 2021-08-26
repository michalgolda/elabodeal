import { createApp } from 'vue'

import Main from './components/Main'

import store from './store'


const app = createApp(Main)

app.use(store)

const mountElement = document.getElementById('mount0_0')

app.mount(mountElement)