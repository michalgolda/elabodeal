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
		/>
	</div>
</template>
<script>
import { mapState } from 'vuex';
import ProductListItem from './ProductListItem';

export default {
	components: {
		ProductListItem
	},
	computed: {
		...mapState(['products']),
		cartIsEmpty () {
			return this.products.length === 0
		}
	}
}
</script>