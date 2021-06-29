<template>
	<input 
		class="switch" 
	    type="checkbox"
	    :name="name"
	    :checked="currentValue"
	    @change="emitChange"
	/>	
</template>
<script>
export default {
	emits: ['change'],
	props: {
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
		emitChange: function ( e ) {
			const input = e.target;
			const { checked: isChecked } = input;

			this.$emit( "change", isChecked );
		}
	}
}
</script>