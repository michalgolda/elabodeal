<template>
	<button 
		class="btn btn__secondary"
		@click="addProductToCart"
	>
		Dodaj do koszyka
	</button>
</template>
<script>
import { toRefs } from 'vue'
import { useStore } from 'vuex'
import { cartModuleTypes } from '../store/modules'


export default {
	props: {
		productId: {
			type: String,
			required: true
		}
	},
	setup (props) {
		const { productId } = toRefs(props)

		const store = useStore()

		const addProductToCart = () => {
			store.dispatch(
				cartModuleTypes.actions.ADD_PRODUCT_TO_CART,
				{ productId: productId.value }
			)
		}

		return { addProductToCart }
	}
}
</script>