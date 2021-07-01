<template>
	<SettingsSection
		name="account_number"
		title="Numer konta"
		description="ajdawjdakwjdk"
		currentLabel="Aktualny numer konta"
		:currentValue="currentValue"
	>
		<form @submit.prevent="handleSaveChanges">
			<div class="form__input-group">
				<label>Aktualny numer konta</label>
				<p
					class="form__input-error-msg"
					v-for="error in accountNumbersErrors"
				>
					{{ error }}
				</p>
				<input 
					type="text"
					name="account_number"
					required="required"
					:class="{'form__input-error': accountNumberErrors}"
					@change="handleChangeAccountNumber"
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
			currentValue: state => state.publisher.account_number
		}),
		...mapUiState({
			accountNumberErrors: state => state.section.error.account_number
		}),
	},
	data() {
		return {
			account_number: ''
		}
	},
	methods: {
		...mapUiMutations(['setSectionError']),
		...mapPublisherSettingsActions(['changeAccountNumber']),
		handleSaveChanges (e) {
			if (!this.account_number || this.account_number === this.currentValue)
				return;

			this.changeAccountNumber({ account_number: this.account_number });
		},
		handleChangeAccountNumber (e) {
			this.account_number = e.target.value;
		}
	}
}
</script>