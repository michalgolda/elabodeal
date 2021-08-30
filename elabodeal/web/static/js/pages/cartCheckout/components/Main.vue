<template>
	<DeliverView v-if="showDeliverView" />
	<PaymentView v-if="showPaymentView" />
	<PaymentSuccessView v-if="showPaymentSuccessView" />
</template>
<script>
import { computed } from 'vue'
import { useStore } from 'vuex'

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
			return store.state.currentStep === 'deliver'
		})

		const showPaymentView = computed(() => {
			return store.state.currentStep === 'payment' && store.state.delivery !== {}
		})

		const showPaymentSuccessView = computed(() => {
			return store.state.currentStep === 'success'
		})

		return {
			showDeliverView,
			showPaymentView,
			showPaymentSuccessView
		}
	}
}
</script>