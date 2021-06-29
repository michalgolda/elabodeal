<template>
	<div 
		class="settings__section"
		:class="{'settings__section-isEditing': isEditing}"
	>
		<template v-if="isEditing">
			<p class="settings__section-title">{{ title }}</p>
			<p class="settings__section-description">
				{{ description }}
			</p>
			<div class="settings__section-content">
				<div v-if="showCurrentValue">
					<label>{{ currentLabel }}</label>
					<input
						type="text"
						disabled="disabled" 
						:name="`current_${name}`"
						:placeholder="currentValue"
					/>
				</div>
				<slot />
				<button 
					class="btn btn-block btn__primary"
					@click="handleCancelEdit"
				>
					Anuluj
				</button>
			</div>
		</template>
		<template v-else>
			<div>
				<p class="settings__section-title">{{ title }}</p>
				<p 
					class="settings__section-currentValue"
					v-if="showCurrentValue"
				>
					{{ currentValue }}
				</p>
			</div>
			<button
				class="btn btn__secondary"
				@click="handleEdit"
			>
				Edytuj
			</button>
		</template>
	</div>
</template>
<script>
import { createNamespacedHelpers } from 'vuex';

const { mapState, mapMutations } = createNamespacedHelpers('ui');


export default {
	props: {
		name: {
			type: String,
			required: true
		},
		title: {
			type: String,
			required: true
		},
		description: {
			type: String,
			required: true
		},
		currentLabel: {
			type: String,
			default: ''
		},
		currentValue: {
			type: String,
			default: ''
		}
	},
	computed: {
		...mapState({
			currentSectionName: state => state.section.name
		}),
		showCurrentValue() {
			return this.currentValue ? true : false;
		},
		isEditing() {
			return this.currentSectionName === this.name;
		}		
	},
	methods: {
		...mapMutations(['showSection', 'hideSection']),
		handleEdit(e) {
			this.showSection(this.name);
		},
		handleCancelEdit(e) {
			this.hideSection();
		}
	}
}
</script>