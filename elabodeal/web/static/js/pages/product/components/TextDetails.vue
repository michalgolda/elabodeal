<template>
	<div class="text-details__actions">
		<button 
			class="btn"
			:class="[showDescription ? 'btn__primary' : 'btn__primary-outline']"
			@click="() => { showDescription = true; }"
		>
			Opis
		</button>
		<button 
			class="btn"
			:class="[!showDescription ? 'btn__primary' : 'btn__primary-outline']"
			@click="() => { showDescription = false; }"
		>
			Spis treści
		</button>
	</div>
	<div 
		v-if="showDescription"
		class="text-details__content"
	>
		<p>{{ description }}</p>
	</div>
	<div 
		v-if="!showDescription"
		class="text-details__content"
	>
		<p>{{ contents }}</p>
	</div>
</template>
<script>
export default {
	props: {
		description: {
			type: String,
			required: true
		},
		contents: {
			type: String,
			required: true
		}
	},
	data () {
		return {
			showDescription: true
		}
	}
}
</script>