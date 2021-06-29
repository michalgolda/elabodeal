<template>
	<SettingsTab
		title="Ustawienia użytkownika"
	>
		<SettingsGroup
			title="Ustawienia konta"
		>
			<SettingsSectionList>
				<UsernameSettingsSection />
				<EmailSettingsSection />
				<PasswordSettingsSection />
			</SettingsSectionList>
		</SettingsGroup>
		<SettingsGroup
			title="Powiadomienia"
		>
			<NewsletterSettingsSection />
		</SettingsGroup>
	</SettingsTab>
</template>
<script>
import SettingsTab from '../SettingsTab';
import SettingsGroup from '../SettingsGroup';
import SettingsSectionList from '../SettingsSectionList';

import EmailSettingsSection from './EmailSettingsSection';
import UsernameSettingsSection from './UsernameSettingsSection';
import PasswordSettingsSection from './PasswordSettingsSection';
import NewsletterSettingsSection from './NewsletterSettingsSection';


export default {
	components: {
		SettingsTab,
		SettingsGroup,
		SettingsSectionList,
		EmailSettingsSection,
		UsernameSettingsSection,
		PasswordSettingsSection,
		NewsletterSettingsSection
	}
}
</script>