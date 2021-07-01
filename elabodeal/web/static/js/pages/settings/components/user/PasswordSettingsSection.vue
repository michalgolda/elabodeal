<template>
	<SettingsSection
		name="password"
		title="Hasło"
		description="Fajny opisik"
	>
		<form @submit.prevent="handleSaveChanges">
			<div class="form__input-group">
				<label>AKTUALNE HASŁO</label>
				<p
					class="form__input-error-msg"
					v-for="error in currentPasswordErrors"
				>
					{{ error }}
				</p>
				<input 
					name="current_password"
					type="password"
					required="required"
					:class="{'form__input-error': currentPasswordErrors}"
					@change="handleChangeCurrentPassword"
				/>
			</div>
			<div class="form__input-group">
				<label>HASŁO</label>
				<p
					class="form__input-error-msg"
					v-for="error in newPasswordErrors"
				>
					{{ error }}
				</p>
				<input 
					name="new_password"
					type="password"
					required="required"
					:class="{'form__input-error': newPasswordErrors}"
					@change="handleChangeNewPassword"
				/>
			</div>
			<div class="form__input-group">
				<label>POWTÓRZ HASŁO</label>
				<p
					class="form__input-error-msg"
					v-for="error in newPasswordRepeatErrors"
				>
					{{ error }}
				</p>
				<input 
					name="new_password_repeat"
					type="password"
					required="required"
					:class="{'form__input-error': newPasswordRepeatErrors}"
					@change="handleChangeNewPasswordRepeat"
				/>
			</div>
			<button class="btn btn-block btn__secondary">Zmień</button>
		</form>
	</SettingsSection>
</template>
<script>
import { createNamespacedHelpers } from 'vuex'; 

import SettingsSection from "../SettingsSection";


const { mapState: mapUiState,
		mapMutations: mapUiMutations } = createNamespacedHelpers('ui');
const { mapActions: mapUserSettingsActions } = createNamespacedHelpers('userSettings');

export default {
	components: {
		SettingsSection
	},
	computed: {
		...mapUiState({
			newPasswordErrors: state => state.section.error.new_password,
			currentPasswordErrors: state => state.section.error.current_password,
			newPasswordRepeatErrors: state => state.section.error.new_password_repeat
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
		...mapUiMutations(['setSectionError']),
		...mapUserSettingsActions(['changePassword']),
		handleSaveChanges (e) {
			if (this.newPassword !== this.newPasswordRepeat) {
				this.setSectionError({
					new_password_repeat: ['Hasła nie są zgodne.']
				});

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