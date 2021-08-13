<template>
	<template v-if="userIsPublisher">
		<SettingsTab
			title="Ustawienia sprzedającego"
		>
			<SettingsSectionList>
				<FirstNameSettingsSection />
				<LastNameSettingsSection />
				<SwiftCodeSettingsSection />
				<AccountNumberSettingsSection />
			</SettingsSectionList>
		</SettingsTab> 
	</template>
	<template v-else>
		<div>
			<p>Utwórz konto sprzedającego. Kliknij w przycisk poniżej.</p>
			<a 
				href="/m/start/"
				class="btn btn__secondary"
			>
				Utwórz
			</a>
		</div>
	</template>
</template>
<script>
import { mapState } from 'vuex';


import SettingsTab from '../SettingsTab';
import SettingsSectionList from '../SettingsSectionList';

import LastNameSettingsSection from './LastNameSettingsSection';
import FirstNameSettingsSection from './FirstNameSettingsSection';
import SwiftCodeSettingsSection from './SwiftCodeSettingsSection';
import AccountNumberSettingsSection from './AccountNumberSettingsSection';


export default {
	components: {
		SettingsTab,
		SettingsSectionList,
		LastNameSettingsSection,
		FirstNameSettingsSection,
		SwiftCodeSettingsSection,
		AccountNumberSettingsSection
	},
	computed: mapState({
		userIsPublisher: state => state.user.is_publisher
	})
}
</script>