<template>
	<SettingsSection
		name="swift_code"
		title="Kod SWIFT"
		description="awdjawkd"
		currentLabel="Aktualny kod SWIFT"
		:currentValue="currentValue"
	>
		<div class="form__input-group">
			<label>KOD SWIFT</label>
			<input 
				name="new_swift_code"
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