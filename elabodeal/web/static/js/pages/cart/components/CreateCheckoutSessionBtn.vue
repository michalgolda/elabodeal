<template>
	<button
		v-if="enabledBtn"
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
import { mainModuleTypes } from '../store/modules'


export default {
	setup () {
		const store = useStore()
	
		const enabledBtn = computed(() => {
			return store.getters[
				mainModuleTypes.getters.CREATE_CHECKOUT_SESSION_BTN_ENABLED
			]
		})

		const createCheckoutSession = () => {
			store.dispatch(
				mainModuleTypes.actions.CREATE_CHECKOUT_SESSION,
				null
			)
		}

		return {
			enabledBtn,
			createCheckoutSession
		}
	}
}
</script>