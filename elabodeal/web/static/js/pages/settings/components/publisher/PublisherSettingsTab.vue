<template>
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
<script>
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
	}
}
</script>