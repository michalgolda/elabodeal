<template>
	<main class="section">
		<p class="section__title">
			{{ title }}
		</p>
		<div class="section__content">
			<slot />
		</div>
	</main>
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