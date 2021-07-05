<template>
	<SettingsSection
		name="email"
		title="Adres email"
		description="Miejsce na fajną informacje"
		current-label="Aktulany adres email"
		:current-value="currentValue"
	>
		<form @submit.prevent="handleSaveChanges">
			<div class="form__input-group">
				<label>EMAIL</label>
				<p
					class="form__input-error-msg"
					v-for="error in emailErrors"
					:key="error"
				>
					{{ error }}
				</p>
				<input 
					name="email"
					type="email"
					required="required"
					:class="{'form__input-error': emailErrors}"
					@change="handleChangeEmail"
				>
			</div>
			<div class="form__input-group">
				<label>POWTÓRZ EMAIL</label>
				<p
					class="form__input-error-msg"
					v-for="error in emailRepeatErrors"
					:key="error"
				>
					{{ error }}
				</p>
				<input 
					name="email_repeat"
					type="email"
					required="required" 
					:class="{'form__input-error': emailRepeatErrors}"
					@change="handleChangeEmailRepeat"
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
			emailErrors: state => state.section.error.email,
			emailRepeatErrors: state => state.section.error.email_repeat
		})
	},
	data () {
		return {
			email: '',
			emailRepeat: ''
		}
	},
	methods: {
		...mapUiMutations(['setSectionError']),
		...mapUserSettingsActions(['changeEmail']),
		handleSaveChanges () {
			if (!this.email || !this.emailRepeat)
				return;

			if (this.email !== this.emailRepeat) {
				this.setSectionError({
					email_repeat: ['Adresy email nie są zgodne.']
				});

				return;
			}

			if (this.emailRepeat === this.currentValue) {
				this.setSectionError({
					email: ['Nowy adres email jest taki sam jak aktualny.'],
					email_repeat: undefined
				});

				return;
			}

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