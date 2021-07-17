<template>
	<DeliverView v-if="showDeliverView" />
	<PaymentView v-if="showPaymentView" />
	<PaymentSuccessView v-if="showPaymentSuccessView" />
</template>
<script>
import { createNamespacedHelpers } from 'vuex';

import DeliverView from './DeliverView';
import PaymentView from './PaymentView';
import PaymentSuccessView from './PaymentSuccessView';

const { mapState: mapUiState } = createNamespacedHelpers('ui');
const { mapState: mapDeliverState } = createNamespacedHelpers('deliver');


export default {
	components: {
		DeliverView,
		PaymentView,
		PaymentSuccessView
	},
	computed: {
		...mapUiState(['currentStep']),
		...mapDeliverState(['collectedDeliverData']),
		showDeliverView () {
			return this.currentStep === 'deliver';
		},
		showPaymentView () {
			return this.currentStep === 'payment' && this.collectedDeliverData;
		},
		showPaymentSuccessView () {
			return this.currentStep === 'success';
		}
	}
}
</script>