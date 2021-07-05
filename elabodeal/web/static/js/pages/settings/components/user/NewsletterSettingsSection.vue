<template>
	<CheckboxSettingsSection 
		name="newsletter"
		title="Newsletter"
		description="Fajny opis tutaj będzie"
		:current-value="currentValue"
		@change="handleChange"
	/>
</template>
<script>
import { 
	createNamespacedHelpers,
	mapState as mapRootState } from 'vuex';

import CheckboxSettingsSection from '../CheckboxSettingsSection';

const { mapActions: mapUserSettingsActions } = createNamespacedHelpers('userSettings');


export default {
	components: {
		CheckboxSettingsSection
	},
	computed: mapRootState({
		currentValue: state => state.user.newsletter
	}),
	methods: {
		...mapUserSettingsActions(['toggleNewsletter']),
		handleChange (value) {
			this.toggleNewsletter({ value });
		}
	}
}
</script>