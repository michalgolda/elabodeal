<template>
	<SettingsSection
		name="first_name"
		title="Imię"
		description="awjdkawjdkaw"
		current-label="Aktualne imię"
		:current-value="currentValue"
	>
		<form @submit.prevent="handleSaveChanges">
			<div class="form__input-group">
				<label>Imię</label>
				<p 
					class="form__input-error-msg"
					v-for="error in firstNameErrors"
					:key="error"
				>
					{{ error }}
				</p>
				<input 
					type="text"
					name="first_name"
					required="required"
					:class="{'form__input-error': firstNameErrors}"
					@change="handleChangeFirstName"
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
			currentValue: state => state.publisher.first_name
		}),
		...mapUiState({
			firstNameErrors: state => state.section.error.first_name
		}),
	},
	data() {
		return {
			first_name: ''
		}
	},
	methods: {
		...mapUiMutations(['setSectionError']),
		...mapPublisherSettingsActions(['changeFirstName']),
	handleSaveChanges () {
			if (!this.first_name || this.first_name === this.currentValue)
				return;

			this.changeFirstName({ first_name: this.first_name });
		},
		handleChangeFirstName (e) {
			this.first_name = e.target.value;
		}
	}
}
</script>