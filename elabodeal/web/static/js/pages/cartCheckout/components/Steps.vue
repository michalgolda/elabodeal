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
import { uiModuleTypes } from '../store/modules';

import StepElement from './StepElement';


export default {
	components: {
		StepElement
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