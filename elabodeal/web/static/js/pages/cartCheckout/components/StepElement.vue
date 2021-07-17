<template>
	<div 
		class="checkout-step flex-center"
		:class="{
			'checkout-step-current': current,
			'checkout-step-succeed': succeed
		}"
	>
		<figure class="flex-center">
			<span class="h2">
				<template v-if="succeed">
					<i class="fas fa-check" />
				</template>
				<template v-else>
					{{ number }}
				</template>
			</span>
		</figure>
		<span class="h2">
			{{ name }}
		</span>
	</div>
</template>
<script>
export default {
	props: {
		name: {
			type: String,
			required: true
		},
		number: {
			type: Number,
			required: true
		},
		current: {
			type: Boolean,
			default: false
		},
		succeed: {
			type: Boolean,
			default: false
		}
	}
}
</script>