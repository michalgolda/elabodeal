<template>
	<button
		v-if="enableBtn"
		class="btn btn__primary"
		@click="handleClick"
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
import { mapActions, mapState } from 'vuex';


export default {
	computed: mapState({
		enableBtn: state => state.selectedProducts.length > 0 && state.products.length > 0
	}),
	methods: {
		...mapActions(['createCheckoutSession']),
		handleClick () {
			this.createCheckoutSession();
		}
	}
}
</script>