import Vue from 'vue';

import EmailConfirmationForm from '../../components/EmailConfirmationForm.vue';


const mountElement = document.getElementById( 'js-mount-form-component' );
const mountData = mountElement.dataset;

const Form = new Vue.extend( EmailConfirmationForm );

const formInstance = new Form( {
	data() {
		return {...mountData};
	}
} );
formInstance.$mount( mountElement );