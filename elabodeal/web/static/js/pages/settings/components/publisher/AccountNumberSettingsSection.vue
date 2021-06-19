<template>
	<SettingsSection
		name="account_number"
		title="Numer konta"
		description="ajdawjdakwjdk"
		currentLabel="Aktualny numer konta"
		:currentValue="currentValue"
	>
		<div class="form__input-group">
			<label>NUMER KONTA BANKOWEGO</label>
			<input 
				name="new_account_number"
				type="text"
			/>
		</div>
	</SettingsSection>
</template>
<script>
import SettingsSection from '../SettingsSection';


export default {
	components: {
		SettingsSection
	},
	data() {
		return {
			currentValue: '123'
		}
	}
}
</script>