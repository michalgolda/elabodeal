<template>
	<div class="section flex-center">
		<StepElement
			:number="1"
			name="Koszyk"
			:succeed="true"
		/>
		<div class="checkout-step__separator" />
		<StepElement
			:number="2" 
			name="Wysyłka"
			:current="currentStepIsDeliver"
			:succeed="currentStepIsPayment || currentStepIsSuccess"
		/>
		<div class="checkout-step__separator" />
		<StepElement
			:number="3" 
			name="Płatność"
			:current="currentStepIsPayment"
			:succeed="currentStepIsSuccess"
		/>
	</div>
</template>
<script>
import { createNamespacedHelpers } from 'vuex';

import StepElement from './StepElement';

const { mapState: mapUiState } = createNamespacedHelpers('ui');


export default {
	components: {
		StepElement
	},
	computed: {
		...mapUiState(['currentStep']),
		currentStepIsDeliver () {
			return this.currentStep === 'deliver';
		},
		currentStepIsPayment () {
			return this.currentStep === 'payment';
		},
		currentStepIsSuccess () {
			return this.currentStep === 'success';
		}
	}
}
</script>