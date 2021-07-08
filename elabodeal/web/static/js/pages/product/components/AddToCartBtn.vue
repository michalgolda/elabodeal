<template>
	<button 
		class="btn btn__secondary"
		@click="handleClick"
	>
		Dodaj do koszyka
	</button>
</template>
<script>
import { createNamespacedHelpers } from 'vuex';

const { mapActions: mapCartActions } = createNamespacedHelpers('cart');


export default {
	props: {
		productId: {
			type: String,
			required: true
		}
	},
	methods: {
		...mapCartActions(['addProductToCart']),
		handleClick () {
			this.addProductToCart({
				productId: this.productId
			});
		}
	}
}
</script>