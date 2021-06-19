<template>
	<SettingsSection
		name="email"
		title="Adres email"
		description="Miejsce na fajną informacje"
		currentLabel="Aktulany adres email"
		:currentValue="currentValue"
		@saveChanges="handleSaveChanges"
	>
		<div class="form__input-group">
			<label>EMAIL</label>
			<input 
				name="new_email"
				type="email"
				required="required"
				:class="{'form__input-error': currentSectionError}"
				@change="handleChangeEmail"
				@keydown="clearCurrentSectionErrors"
			/>
		</div>
		<div class="form__input-group">
			<label>POWTÓRZ EMAIL</label>
			<input 
				name="new_email_repeat"
				type="email"
				required="required" 
				:class="{'form__input-error': currentSectionError}"
				@change="handleChangeEmailRepeat"
				@keydown="clearCurrentSectionErrors"
			/>
		</div>
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
		...mapUiState(['currentSectionError'])
	},
	data () {
		return {
			email: '',
			emailRepeat: ''
		}
	},
	methods: {
		...mapUiMutations(['setCurrentSectionError']),
		...mapUserSettingsActions(['changeEmail']),
		handleSaveChanges (e) {
			if (!this.email || !this.emailRepeat)
				return;

			if (this.email !== this.emailRepeat) {
				this.setCurrentSectionError(true);

				return;
			}

			if (this.emailRepeat === this.currentValue)
				return;

			this.changeEmail(this.emailRepeat);
		},
		handleChangeEmail (e) {
			this.email = e.target.value;
		},
		handleChangeEmailRepeat (e) {
			this.emailRepeat = e.target.value;
		},
		clearCurrentSectionErrors (e) {
			this.setCurrentSectionError(null);
		}
	}
}
</script>