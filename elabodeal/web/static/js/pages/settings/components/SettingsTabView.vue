<template>
	<UserSettingsTab v-if="currentTabName === 'user'" />
	<PublisherSettingsTab v-if="currentTabName === 'publisher'" />
</template>
<script>
import { createNamespacedHelpers } from 'vuex'

const { mapMutations, mapGetters } = createNamespacedHelpers('ui');

import UserSettingsTab from './user/UserSettingsTab';
import PublisherSettingsTab from './publisher/PublisherSettingsTab';


export default {
	components: {
		UserSettingsTab,
		PublisherSettingsTab
	},
	created() {
		const urlSearchParams = new URLSearchParams(window.location.search);

		const tabParam = urlSearchParams.get('tab');
		const sectionParam = urlSearchParams.get('section');

		this.showTab(tabParam);
		this.showSection(sectionParam);
	},
	computed: mapGetters(['currentTabName']),
	methods: mapMutations([
		'showTab', 
		'showSection'
	])

}
</script>