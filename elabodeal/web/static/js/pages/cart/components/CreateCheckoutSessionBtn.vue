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


export default {
	setup () {
		const store = useStore()

		const btnIsEnabled = computed(() => {
			const selectedProducts = store.getters.getSelectedProducts

			return selectedProducts.length > 0
		})

		const createCheckoutSession = () => {
			store.dispatch('createCheckoutSession')
		}

		return {
			btnIsEnabled,
			createCheckoutSession
		}
	}
}
</script>