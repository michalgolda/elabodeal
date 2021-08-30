<template>
	<div class="section section-summary">
		<p class="summary-title">
			Podsumowanie zakupów
		</p>
		<div
			class="summary-products"
			:style="{ 'overflow-y': summaryProducts.length >= 5 ? 'scroll' : 'hidden' }"
		>
			<ProductSummaryListItem
				v-for="product in summaryProducts"
				:key="product.title"
				:title="product.title"
				:price="product.price"
			/>
		</div>
		<div class="summary-total-price">
			<p>
				Razem: 
				<span class="summary-total-price__highlight">
					{{ summaryTotalPrice }} zł
				</span>
			</p>
		</div>
	</div>
</template>
<script>
import { computed } from 'vue'
import { useStore } from 'vuex'

import ProductSummaryListItem from './ProductSummaryListItem';


export default {
	components: {
		ProductSummaryListItem
	},
	setup () {
		const store = useStore()

		const summaryProducts = computed(() => {
			return store.state.summaryProducts
		})

		const summaryTotalPrice = computed(() => {
			return store.state.summaryTotalPrice
		})

		return {
			summaryProducts,
			summaryTotalPrice
		}
	}
}
</script>