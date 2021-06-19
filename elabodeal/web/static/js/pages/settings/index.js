import { createApp, h as createElement } from 'vue';

import Modal from '@/components/Modal';

import store from './store';
import Main from './components/Main';


const mountElement = document.getElementById('mount0_0');

const vueInstance = createApp({
	render() {
		return createElement(Main);
	}
});

vueInstance.use(store);
vueInstance.use(Modal);

vueInstance.mount(mountElement);