<template>
	<SettingsSection
		name="last_name"
		title="Nazwisko"
		description="awjdkawjdkaw"
		currentLabel="Aktualne nazwisko"
		:currentValue="currentValue"
	>
		<div class="form__input-group">
			<label>Nazwisko</label>
			<input 
				name="new_last_name"
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
			currentValue: 'Gołda'
		}
	}
}
</script>