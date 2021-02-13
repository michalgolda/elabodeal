import Vue from 'vue';

import EmailConfirmationForm from '../../components/EmailConfirmationForm.vue';


const mountElement = document.getElementById( 'js-mount-form-component' );
const mountData = mountElement.dataset;

new Vue({
    el: mountElement,
    render: function( createElement ) {
        return createElement(EmailConfirmationForm, {
            props: {...mountData}
        })
    }
})