<template>
	<SettingsSection 
		name="username"
		title="Nazwa użytkownika"
		description="Fajny opis tutaj będzie"
		current-label="Aktualna nazwa użytkownika"
		:current-value="currentValue"
	>
		<form @submit.prevent="handleSaveChanges">
			<div class="form__input-group">
				<label>nazwa użytkownika</label>
				<p 
					class="form__input-error-msg"
					v-for="error in usernameErrors"
					:key="error"
				>
					{{ error }}
				</p>
				<input 
					type="text"
					name="username"
					required="required"
					:class="{'form__input-error': usernameErrors}"
					@change="handleChangeUsername"
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
const { mapActions: mapUserSettingsActions } = createNamespacedHelpers('userSettings');


export default {
	components: {
		SettingsSection
	},
	data() {
		return {
			username: ''
		}
	},
	computed: {
		...mapRootState({
			currentValue: state => state.user.username
		}),
		...mapUiState({
			usernameErrors: state => state.section.error.username
		}),
	},
	methods: {
		...mapUiMutations(['setSectionError']),
		...mapUserSettingsActions(['changeUsername']),
		handleSaveChanges () {
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