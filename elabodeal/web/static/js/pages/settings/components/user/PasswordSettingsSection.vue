<template>
	<SettingsSection
		name="password"
		title="Hasło"
		description="Fajny opisik"
	>
		<div class="form__input-group">
			<label>Aktualne hasło</label>
			<input 
				name="current_password"
				type="password"
			/>
		</div>
		<div class="form__input-group">
			<label>HASŁO</label>
			<input 
				name="new_password"
				type="password"
			/>
		</div>
		<div class="form__input-group">
			<label>POWTÓRZ HASŁO</label>
			<input 
				name="new_password_repeat"
				type="password"
			/>
		</div>
	</SettingsSection>
</template>
<script>
import SettingsSection from '../SettingsSection';


export default {
	components: {
		SettingsSection
	}
}
</script>