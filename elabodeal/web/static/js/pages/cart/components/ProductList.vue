<template>
	<div 
		v-if="cartIsEmpty"
		class="empty-cart flex-center"
	>
		<p class="h2">
			Twój koszyk jest pusty 😯
		</p>
	</div>
	<div
		v-else
		class="cart-items"
	>
		<ProductListItem 
			v-for="product in products"
			:key="product.id"
			:title="product.title"
			:author="product.author"
			:price="product.price"
			:cover-img-path="product.cover_img.path"
			:product-id="product.id"
			:selected="product.selected"
		/>
	</div>
</template>
<script>
import { computed } from 'vue'
import { useStore } from 'vuex'
import { mainModuleTypes } from '../store/modules'

import ProductListItem from './ProductListItem'


export default {
	components: {
		ProductListItem
	},
	setup () {
		const store = useStore()

		const products = computed(() => {
			return store.getters[mainModuleTypes.getters.GET_PRODUCTS]
		})

		const cartIsEmpty = computed(() => {
			return store.getters[mainModuleTypes.getters.CART_IS_EMPTY]
		})

		return {
			products,
			cartIsEmpty
		}
	}
}
</script>