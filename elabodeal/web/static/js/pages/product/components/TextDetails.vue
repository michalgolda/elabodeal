<template>
	<div class="text-details__actions">
		<button 
			class="btn"
			:class="[descriptionIsVisible ? 'btn__primary' : 'btn__primary-outline']"
			@click="showDescription"
		>
			Opis
		</button>
		<button 
			class="btn"
			:class="[contentsIsVisible ? 'btn__primary' : 'btn__primary-outline']"
			@click="showContents"
		>
			Spis treści
		</button>
	</div>
	<div 
		v-if="descriptionIsVisible"
		class="text-details__content"
	>
		<p>{{ description }}</p>
	</div>
	<div 
		v-if="contentsIsVisible"
		class="text-details__content"
	>
		<p>{{ contents }}</p>
	</div>
</template>
<script>
import { computed } from 'vue'
import { useStore } from 'vuex'
import { uiModuleTypes } from '../store/modules'


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
	setup (props) {
		const { description, contents } = props

		const store = useStore()

		const showContents = () => {
			store.commit(
				uiModuleTypes.mutations.SHOW_CONTENTS
			)
		}

		const showDescription = () => {
			store.commit(
				uiModuleTypes.mutations.SHOW_DESCRIPTION
			)
		}
		
		const contentsIsVisible = computed(() => {
			return store.getters[uiModuleTypes.getters.SHOW_CONTENTS]
		})

		const descriptionIsVisible = computed(() => {
			return store.getters[uiModuleTypes.getters.SHOW_DESCRIPTION]
		})

		return { 
			contents,
			description,
			showContents,
			showDescription,
			contentsIsVisible,
			descriptionIsVisible
		}
	}
}
</script>