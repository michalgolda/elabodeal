<template>
	<li class="settings-list__item settings-list__item-box">
		<div class="settings-item__common">
			<div class="settings-item__common-info">
				<p class="settings-item__title">{{ title }}</p>
				<p class="settings-item__description">{{ description }}</p>
			</div>
			<div class="settings-item__common-center">
				<SwitchInput 
					:name="name"
					:currentValue="currentValue"
				/>
			</div>
		</div>
	</li>
</template>
<script>
import SwitchInput from '@/components/SwitchInput';


export default {
	components: {
		SwitchInput
	},
	props: {
		title: {
			type: String,
			required: true
		},
		description: {
			type: String,
			required: true
		},
		name: {
			type: String,
			required: true
		},
		currentValue: {
			type: Boolean,
			required: true
		}
	}
}
</script>