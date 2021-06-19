<template>
	<li class="settings-list__item settings-list__item-box">
		<div
			class="settings-item__content" 
			v-if="showCurrentSection"
		>
			<p class="settings-item__title">{{ title }}</p>
			<p class="settings-item__description">{{ description }}</p>
			<div class="settings-item__forms">
				<div 
					class="form__input-group"
					v-if="showCurrentValue"
				>
					<label>{{ currentLabel }}</label>
					<input
						type="text"
						disabled="disabled" 
						:name="`current_${name}`"
						:placeholder="currentValue"
					/>
				</div>
				<slot />
				<div class="form__input-group">
					<button 
						class="btn btn-block btn__secondary"
						@click="emitSaveChanges"
					>
						Zapisz zmiany
					</button>
				</div>
				<div class="form__input-group">
					<button
						class="btn btn-block btn__primary"
						@click="handleCancelEdit"
					>
						Anuluj
					</button>
				</div>
			</div>
		</div>
		<div
			class="settings-item__common"
			v-else
		>
			<div 
				class="settings-item__common-info"
				:class="{ 'settings-item__common-center': !showCurrentValue }"
			>
				<p class="settings-item__title">{{ title }}</p>
				<span 
					class="settings-item__preview"
					v-if="showCurrentValue"
				>
					{{ currentValue }}
				</span>
			</div>
			<div class="settings-item__common-center">
				<button
					class="btn btn-block btn__secondary"
					@click="handleEdit"
				>
					Edytuj
				</button>
			</div>
		</div>
	</li>
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
		...mapState(['currentTab', 'currentSection']),
		showCurrentValue() {
			return this.currentValue ? true : false;
		},
		showCurrentSection() {
			return this.currentSection === this.name;
		}		
	},
	methods: {
		...mapMutations(['setCurrentSection']),
		handleEdit(e) {
			this.setCurrentSection(this.name);
		},
		handleCancelEdit(e) {
			this.setCurrentSection(null);
		},
		emitSaveChanges(e) {
			this.$emit('saveChanges', e);
		}
	}
}
</script>