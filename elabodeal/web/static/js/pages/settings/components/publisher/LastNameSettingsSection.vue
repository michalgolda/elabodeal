<template>
	<SettingsSection
		name="last_name"
		title="Nazwisko"
		description="awjdkawjdkaw"
		currentLabel="Aktualne nazwisko"
		:currentValue="currentValue"
	>
		<form @submit.prevent="handleSaveChanges">
			<div class="form__input-group">
				<label>Nazwisko</label>
				<p 
					class="form__input-error-msg"
					v-for="error in lastNameErrors"
				>
					{{ error }}
				</p>
				<input 
					type="text"
					name="last_name"
					required="required"
					:class="{'form__input-error': lastNameErrors}"
					@change="handleChangeLastName"
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
			currentValue: state => state.publisher.last_name
		}),
		...mapUiState({
			lastNameErrors: state => state.section.error.last_name
		}),
	},
	data() {
		return {
			last_name: ''
		}
	},
	methods: {
		...mapUiMutations(['setSectionError']),
		...mapPublisherSettingsActions(['changeLastName']),
		handleSaveChanges (e) {
			if (!this.last_name || this.last_name === this.currentValue)
				return;

			this.changeLastName({ last_name: this.last_name });
		},
		handleChangeLastName (e) {
			this.last_name = e.target.value;
		}
	}
}
</script>