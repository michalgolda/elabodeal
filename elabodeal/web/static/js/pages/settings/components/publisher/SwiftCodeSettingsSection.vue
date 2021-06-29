<template>
	<SettingsSection
		name="swift"
		title="Kod SWIFT"
		description="awdjawkd"
		currentLabel="Aktualny kod SWIFT"
		:currentValue="currentValue"
	>
		<form @submit.prevent="handleSaveChanges">
			<div class="form__input-group">
				<label>Aktualny kod swift</label>
				<input 
					type="text"
					name="swift"
					required="required"
					:class="{'form__input-error': currentSectionError}"
					@change="handleChangeSwift"
					@keydown="() => hideCurrentSectionError"
				/>
			</div>
			<button class="btn btn-block btn__secondary">
				Zmień
			</button>
		</form>
	</SettingsSection>
</template>
<script>
import { 
	createNamespacedHelpers,
	mapState as mapRootState } from 'vuex';

import SettingsSection from '../SettingsSection';

const { mapState: mapUiState,
		mapMutations: mapUiMutations } = createNamespacedHelpers('ui');
const { mapActions: mapPublisherSettingsActions } = createNamespacedHelpers('publisherSettings');


export default {
	components: {
		SettingsSection
	},
	computed: {
		...mapRootState({
			currentValue: state => state.publisher.swift
		}),
		...mapUiState({
			currentSectionError: state => state.section.error.code === 'INVALID_FORM_DATA'
		}),
	},
	data() {
		return {
			swift: ''
		}
	},
	methods: {
		...mapUiMutations([
			'setSectionError', 
			'clearSectionError'
		]),
		...mapPublisherSettingsActions(['changeSwift']),
		handleSaveChanges (e) {
			if (!this.swift || this.swift === this.currentValue)
				return;

			this.changeSwift({
				swift: this.swift
			});
		},
		handleChangeSwift (e) {
			this.swift = e.target.value;
		}
	}
}
</script>