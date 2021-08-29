<template>
	<div class="text-details__actions">
		<button 
			class="btn"
			:class="[state.showDescription ? 'btn__primary' : 'btn__primary-outline']"
			@click="showDescription"
		>
			Opis
		</button>
		<button 
			class="btn"
			:class="[state.showContents ? 'btn__primary' : 'btn__primary-outline']"
			@click="showContents"
		>
			Spis treści
		</button>
	</div>
	<div 
		v-if="state.showDescription"
		class="text-details__content"
	>
		<p>{{ description }}</p>
	</div>
	<div 
		v-if="state.showContents"
		class="text-details__content"
	>
		<p>{{ contents }}</p>
	</div>
</template>
<script>
import { ref } from 'vue'


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
	setup () {
		const state = ref({
			showDescription: true,
			showContents: false
		})

		function showDescription () { 
			state.value.showContents = false
			state.value.showDescription = true
		}

		function showContents () { 
			state.value.showContents = true
			state.value.showDescription = false
		}

		return {
			state,
			showContents,
			showDescription
		}
	}
}
</script>