import { createApp } from 'vue'

import store from './store'

import Main from './components/Main'


const app = createApp(Main)

app.use(store)

const mountElement = document.getElementById('mount0_0')

app.mount(mountElement)