<template>
	<SettingsSection
		name="first_name"
		title="Imię"
		description="awjdkawjdkaw"
		currentLabel="Aktualne imię"
		:currentValue="currentValue"
	>
		<div class="form__input-group">
			<label>IMIĘ</label>
			<input 
				name="new_first_name"
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
			currentValue: 'Michał'
		}
	}
}
</script>