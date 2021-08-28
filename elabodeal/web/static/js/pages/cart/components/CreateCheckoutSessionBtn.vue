<template>
	<button
		v-if="btnIsEnabled"
		class="btn btn__primary"
		@click="createCheckoutSession"
	>
		Przejdź dalej
	</button>
	<button
		v-else
		class="btn btn__disabled"
		disabled
	>
		Przejdź dalej
	</button>
</template>
<script>
import { computed } from 'vue'
import { useStore } from 'vuex'

import { gettersTypes, actionsTypes } from '../store/types'


export default {
	setup () {
		const store = useStore()

		const btnIsEnabled = computed(() => {
			const selectedProducts = store.getters[
				gettersTypes.GET_SELECTED_PRODUCTS
			]

			return selectedProducts.length > 0
		})

		const createCheckoutSession = () => {
			store.dispatch(actionsTypes.CREATE_CHECKOUT_SESSION)
		}

		return {
			btnIsEnabled,
			createCheckoutSession
		}
	}
}
</script>