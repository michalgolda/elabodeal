<template>
	<div class="settings__section">
		<div>
			<p class="settings__section-title">{{ title }}</p>
			<p class="settings__section-description">{{ description }}</p>
		</div>
		<SwitchInput 
			:name="name"
			:currentValue="currentValue"
			@change="emitChange"
		/>
	</div>
</template>
<script>
import SwitchInput from '@/components/SwitchInput';


export default {
	emits: ['change'],
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
	},
	methods: {
		emitChange (value) {
			this.$emit("change", value);
		}
	}
}
</script>