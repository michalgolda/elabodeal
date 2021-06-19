<template>
	<div class="section">
		<p class="section__title section-settings__title">{{ title }}</p>
		<div class="section__content">
			<slot />
		</div>
	</div>
</template>
<script>
export default {
	props: {
		title: {
			type: String,
			required: true
		}
	}
}
</script>