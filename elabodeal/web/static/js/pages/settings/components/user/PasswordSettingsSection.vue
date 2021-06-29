<template>
	<SettingsSection
		name="password"
		title="Hasło"
		description="Fajny opisik"
	>
		<form @submit.prevent="handleSaveChanges">
			<div class="form__input-group">
				<label>AKTUALNE HASŁO</label>
				<input 
					name="current_password"
					type="password"
					required="required"
					:class="{'form__input-error': currentSectionError}"
					@change="handleChangeCurrentPassword"
					@keydown="() => clearSectionError()"
				/>
			</div>
			<div class="form__input-group">
				<label>HASŁO</label>
				<input 
					name="new_password"
					type="password"
					required="required"
					:class="{'form__input-error': currentSectionError}"
					@change="handleChangeNewPassword"
					@keydown="() => clearSectionError()"
				/>
			</div>
			<div class="form__input-group">
				<label>POWTÓRZ HASŁO</label>
				<input 
					name="new_password_repeat"
					type="password"
					required="required"
					:class="{'form__input-error': currentSectionError}"
					@change="handleChangeNewPasswordRepeat"
					@keydown="() => clearSectionError()"
				/>
			</div>
			<button class="btn btn-block btn__secondary">Zmień</button>
		</form>
	</SettingsSection>
</template>
<script>
import { createNamespacedHelpers, 
		 mapState as mapRootState } from 'vuex'; 

import SettingsSection from "../SettingsSection";


const { mapState: mapUiState,
		mapMutations: mapUiMutations } = createNamespacedHelpers('ui');
const { mapActions: mapUserSettingsActions } = createNamespacedHelpers('userSettings');

export default {
	components: {
		SettingsSection
	},
	computed: {
		...mapRootState({
			currentValue: state => state.user.email
		}),
		...mapUiState({
			currentSectionError: state => state.section.error.code === 'INVALID_FORM_DATA'
		})
	},
	data () {
		return {
			currentPassword: '',
			newPassword: '',
			newPasswordRepeat: ''
		}
	},
	methods: {
		...mapUiMutations([
			'setSectionError',
			'clearSectionError'
		]),
		...mapUserSettingsActions(['changePassword']),
		handleSaveChanges (e) {
			if (this.newPassword !== this.newPasswordRepeat) {
				this.setSectionError('INVALID_FORM_DATA');

				return;
			}

			this.changePassword({
				newPassword: this.newPassword,
				currentPassword: this.currentPassword
			});
		},
		handleChangeCurrentPassword (e) {
			this.currentPassword = e.target.value;
		},
		handleChangeNewPassword (e) {
			this.newPassword = e.target.value;
		},
		handleChangeNewPasswordRepeat (e) {
			this.newPasswordRepeat = e.target.value;
		}
	}
}
</script>