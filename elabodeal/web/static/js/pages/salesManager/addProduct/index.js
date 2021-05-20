import { createApp, h as createElement } from "vue";

import store from "./store";
import Main from "./components/Main.vue";


const mountElement = document.getElementById( "mount0_0" );

const vueInstance = createApp( {
	render: function () {
		return createElement( Main );
	}
} );

vueInstance.use(store);
vueInstance.mount( mountElement );