<template>
	<SettingsSection 
		name="username"
		title="Nazwa użytkownika"
		description="Fajny opis tutaj będzie"
		currentLabel="Aktualna nazwa użytkownika"
		:currentValue="currentValue"
	>
		<form @submit.prevent="handleSaveChanges">
			<div class="form__input-group">
				<label>nazwa użytkownika</label>
				<input 
					type="text"
					name="username"
					required="required"
					:class="{'form__input-error': currentSectionError}"
					@change="handleChangeUsername"
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
const { mapActions: mapUserSettingsActions } = createNamespacedHelpers('userSettings');


export default {
	components: {
		SettingsSection
	},
	computed: {
		...mapRootState({
			currentValue: state => state.user.username
		}),
		...mapUiState({
			currentSectionError: state => state.section.error.code === 'INVALID_FORM_DATA'
		}),
	},
	data() {
		return {
			username: ''
		}
	},
	methods: {
		...mapUiMutations([
			'setSectionError', 
			'clearSectionError'
		]),
		...mapUserSettingsActions(['changeUsername']),
		handleSaveChanges (e) {
			if (!this.username || this.username === this.currentValue)
				return;

			this.changeUsername({
				username: this.username
			});
		},
		handleChangeUsername (e) {
			this.username = e.target.value;
		}
	}
}
</script>