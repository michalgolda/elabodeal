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
			:current="showDeliverView"
			:succeed="showPaymentView || showPaymentSuccessView"
		/>
		<div class="checkout-step__separator" />
		<StepElement
			:number="3" 
			name="Płatność"
			:current="showPaymentView"
			:succeed="showPaymentSuccessView"
		/>
	</div>
</template>
<script>
import { computed } from 'vue'
import { useStore } from 'vuex'

import StepElement from './StepElement';


export default {
	components: {
		StepElement
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