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
import { paymentModuleTypes } from '../store/modules';

import ProductSummaryListItem from './ProductSummaryListItem';


export default {
	components: {
		ProductSummaryListItem
	},
	setup () {
		const store = useStore()

		const summaryProducts = computed(() => {
			return store.getters[
				paymentModuleTypes.getters.GET_SUMMARY_PRODUCTS
			]
		})

		const summaryTotalPrice = computed(() => {
			return store.getters[
				paymentModuleTypes.getters.GET_SUMMARY_TOTAL_PRICE
			]
		})

		return {
			summaryProducts,
			summaryTotalPrice
		}
	}
}
</script>