<template>
	<div class="wrapper">
		<SettingsTabMenu />
		<SettingsTabView />
	</div>
</template>
<script>
import SettingsTabMenu from "./SettingsTabMenu";
import SettingsTabView from "./SettingsTabView";


export default {
	components: {
		SettingsTabMenu,
		SettingsTabView
	}
}
</script>