<template>
	<div class="summary-product">
		<span class="summary-product__title">{{ title }}</span>
		<span class="summary-product__price">{{ price }} zł</span>
	</div>
</template>
<script>
export default {
	props: {
		title: {
			type: String,
			required: true
		},
		price: {
			type: Number,
			required: true
		}
	}
}
</script>