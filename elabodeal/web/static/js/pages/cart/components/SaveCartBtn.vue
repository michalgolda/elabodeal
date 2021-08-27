<template>
	<button 
		v-if="cartIsNotEmpty"
		class="btn btn__primary"
		@click="showModal"
	>
		Zapisz koszyk
	</button>
</template>
<script>
import { computed, inject } from 'vue'
import { useStore } from 'vuex'


export default {
	setup () {
		const store = useStore()

		const $modalManager = inject('$modalManager')

		const showModal = () => {
			$modalManager.show('saveCartModal')
		}

		const cartIsNotEmpty = computed(() => {
			return store.state.products.length > 0
		})
		
		return {
			showModal,
			cartIsNotEmpty
		}
	}
}
</script>