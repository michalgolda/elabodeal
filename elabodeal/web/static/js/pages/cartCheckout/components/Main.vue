<template>
	<DeliverView v-if="showDeliverView" />
	<PaymentView v-if="showPaymentView" />
	<PaymentSuccessView v-if="showPaymentSuccessView" />
</template>
<script>
import { computed } from 'vue'
import { useStore } from 'vuex'
import { uiModuleTypes } from '../store/modules';

import DeliverView from './DeliverView';
import PaymentView from './PaymentView';
import PaymentSuccessView from './PaymentSuccessView';


export default {
	components: {
		DeliverView,
		PaymentView,
		PaymentSuccessView
	},
	setup () {
		const store = useStore()

		const showDeliverView = computed(() => {
			return store.getters[uiModuleTypes.getters.SHOW_DELIVER_VIEW]
		})

		const showPaymentView = computed(() => {
			return store.getters[uiModuleTypes.getters.SHOW_PAYMENT_VIEW]
		})

		const showPaymentSuccessView = computed(() => {
			return store.getters[uiModuleTypes.getters.SHOW_PAYMENT_SUCCESS_VIEW]
		})

		return {
			showDeliverView,
			showPaymentView,
			showPaymentSuccessView
		}
	}
}
</script>