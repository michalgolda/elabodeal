<template>
	<SettingsSection
		name="email"
		title="Adres email"
		description="Miejsce na fajną informacje"
		currentLabel="Aktulany adres email"
		:currentValue="currentValue"
	>
		<form @submit.prevent="handleSaveChanges">
			<div class="form__input-group">
				<label>EMAIL</label>
				<input 
					name="email"
					type="email"
					required="required"
					:class="{'form__input-error': currentSectionError}"
					@change="handleChangeEmail"
					@keydown="() => clearSectionError()"
				/>
			</div>
			<div class="form__input-group">
				<label>POWTÓRZ EMAIL</label>
				<input 
					name="email_repeat"
					type="email"
					required="required" 
					:class="{'form__input-error': currentSectionError}"
					@change="handleChangeEmailRepeat"
					@keydown="() => clearSectionError()"
				/>
			</div>
			<button class="btn btn-block btn__secondary">
				Zmień
			</button>
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
			email: '',
			emailRepeat: ''
		}
	},
	methods: {
		...mapUiMutations([
			'setSectionError',
			'clearSectionError'
		]),
		...mapUserSettingsActions(['changeEmail']),
		handleSaveChanges (e) {
			if (!this.email || !this.emailRepeat)
				return;

			if (this.email !== this.emailRepeat) {
				this.setSectionError('INVALID_FORM_DATA');

				return;
			}

			if (this.emailRepeat === this.currentValue)
				return;

			this.changeEmail({
				email: this.email
			});
		},
		handleChangeEmail (e) {
			this.email = e.target.value;
		},
		handleChangeEmailRepeat (e) {
			this.emailRepeat = e.target.value;
		}
	}
}
</script>