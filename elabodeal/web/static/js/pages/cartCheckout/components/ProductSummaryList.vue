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
import { createNamespacedHelpers } from 'vuex';

import ProductSummaryListItem from './ProductSummaryListItem';

const { mapState: mapPaymentState } = createNamespacedHelpers('payment');


export default {
	components: {
		ProductSummaryListItem
	},
	computed: mapPaymentState([
		'summaryProducts', 
		'summaryTotalPrice'
	])
}
</script>