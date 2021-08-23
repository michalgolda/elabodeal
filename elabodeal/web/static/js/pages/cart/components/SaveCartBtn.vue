<template>
	<button 
		v-if="cartIsNotEmpty"
		class="btn btn__primary"
		@click="handleClick"
	>
		Zapisz koszyk
	</button>
</template>
<script>
export default {
	setup () {
		const store = useStore()

		const showModal = () => {
			this.$modalManager.show('saveCartModal')
		}

		const cartIsNotEmpty = () => {
			return !store.getters[mainModuleTypes.getters.CART_IS_EMPTY]
		}
		
		return {
			showModal,
			cartIsNotEmpty
		}
	}
}
</script>