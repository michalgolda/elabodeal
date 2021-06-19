<template>
	<SettingsSection 
		name="username"
		title="Nazwa użytkownika"
		description="Fajny opis tutaj będzie"
		currentLabel="Aktualna nazawa użytkownika"
		:currentValue="currentValue"
		@saveChanges="handleSaveChanges"
	>
		<div class="form__input-group">
			<label>NAZWA UŻYTKOWNIKA</label>
			<input 
				name="new_username"
				type="text"
				required="required"
				:class="{'form__input-error': currentSectionError}"
				@change="handleChangeUsername"
				@keydown="clearCurrentSectionErrors"
			/>
		</div>
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
		...mapUiState(['currentSectionError'])
	},
	data() {
		return {
			username: ''
		}
	},
	methods: {
		...mapUiMutations(['setCurrentSectionError']),
		...mapUserSettingsActions(['changeUsername']),
		handleSaveChanges (e) {
			if (!this.username || this.username === this.currentValue)
				return;

			this.changeUsername(this.username);
		},
		handleChangeUsername (e) {
			this.username = e.target.value;
		},
		clearCurrentSectionErrors (e) {
			this.setCurrentSectionError(null);
		}
	}
}
</script>