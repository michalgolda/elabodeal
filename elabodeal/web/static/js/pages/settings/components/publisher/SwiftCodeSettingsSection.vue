<template>
	<SettingsSection
		name="swift"
		title="Kod SWIFT"
		description="awdjawkd"
		current-label="Aktualny kod SWIFT"
		:current-value="currentValue"
	>
		<form @submit.prevent="handleSaveChanges">
			<div class="form__input-group">
				<label>Aktualny kod swift</label>
				<p
					class="form__input-error-msg"
					v-for="error in swiftErrors"
					:key="error"
				>
					{{ error }}
				</p>
				<input 
					type="text"
					name="swift"
					required="required"
					:class="{'form__input-error': swiftErrors}"
					@change="handleChangeSwift"
				>
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
			swiftErrors: state => state.section.error.swift
		}),
	},
	data() {
		return {
			swift: ''
		}
	},
	methods: {
		...mapUiMutations(['setSectionError']),
		...mapPublisherSettingsActions(['changeSwift']),
		handleSaveChanges () {
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