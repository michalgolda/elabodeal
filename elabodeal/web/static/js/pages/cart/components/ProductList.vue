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
			:cover-img-path="product.cover_img_path"
			:product-id="product.id"
			:selected="product.selected"
		/>
	</div>
</template>
<script>
import { computed } from 'vue'
import { useStore } from 'vuex'

import ProductListItem from './ProductListItem'


export default {
	components: {
		ProductListItem
	},
	setup () {
		const store = useStore()

		const products = computed(() => {
			return store.state.products
		})

		const cartIsEmpty = computed(() => {
			return store.state.products.length === 0
		})

		return {
			products,
			cartIsEmpty
		}
	}
}
</script>