import Vue from "vue";
import Form from '../form';

// Plugins
import Modal from '../../../modal';

// Components
import EmailConfirmationModal from './components/EmailConfirmationModal.vue';

// Load plugins
Vue.use( Modal );


const mountElement = Form.extendOptions.defaultMountElement;

const formInstance = new Form( {
	components: {
		EmailConfirmationModal
	}
} );
formInstance.$mount( mountElement );