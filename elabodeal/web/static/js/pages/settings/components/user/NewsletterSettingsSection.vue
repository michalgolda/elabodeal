<template>
	<CheckboxSettingsSection 
		name="newsletter"
		title="Newsletter"
		description="Fajny opis tutaj będzie"
		:currentValue="currentValue"
	/>
</template>
<script>
import CheckboxSettingsSection from '../CheckboxSettingsSection';


export default {
	components: {
		CheckboxSettingsSection
	},
	data() {
		return {
			currentValue: true
		}
	}
}
</script>