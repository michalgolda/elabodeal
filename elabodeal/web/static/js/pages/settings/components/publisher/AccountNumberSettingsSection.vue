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
				<input 
					type="text"
					name="account_number"
					required="required"
					:class="{'form__input-error': currentSectionError}"
					@change="handleChangeAccountNumber"
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
			currentValue: state => state.publisher.account_number
		}),
		...mapUiState({
			currentSectionError: state => state.section.error.code === 'INVALID_FORM_DATA'
		}),
	},
	data() {
		return {
			account_number: ''
		}
	},
	methods: {
		...mapUiMutations([
			'setSectionError', 
			'clearSectionError'
		]),
		...mapPublisherSettingsActions(['changeAccountNumber']),
		handleSaveChanges (e) {
			if (!this.account_number || this.account_number === this.currentValue)
				return;

			this.changeAccountNumber({
				account_number: this.account_number
			});
		},
		handleChangeAccountNumber (e) {
			this.account_number = e.target.value;
		}
	}
}
</script>