<template>
	<UserSettingsTab v-if="currentTab === 'user'" />
	<PublisherSettingsTab v-if="currentTab === 'publisher'" />
</template>
<script>
import { createNamespacedHelpers } from 'vuex'

const { mapState, mapMutations } = createNamespacedHelpers('ui');

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

		this.setCurrentTab(tabParam);
		this.setCurrentSection(sectionParam);
	},
	computed: mapState(['currentTab']),
	methods: mapMutations(['setCurrentTab', 'setCurrentSection'])

}
</script>