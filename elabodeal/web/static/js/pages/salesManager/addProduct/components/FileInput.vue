<template>
	<input 
		style="display: none;"
		ref="input" 
		type="file" 
		:accept="accept"
		@change="handleUploadedFile"
	/>
	<slot
		:handleChooseFile="handleChooseFile"
		:handleDeleteFile="handleDeleteFile"
		:isEmpty="isEmpty" 
	/>
</template>
<script>
export default {
	props: {
		accept: String
	},
	data: function () {
		return {
			isEmpty: true
		}
	},
	emits: [ "choose", "delete" ],
	methods: {
		handleChooseFile: function ( e ) {
			const { input } = this.$refs;

			input.click();
		},
		handleDeleteFile: function ( e ) {
			const { input } = this.$refs;

			const file = input.files[ 0 ];

			input.value = '';

			this.$emit( "delete", { file, e } );

			this.isEmpty = true;
		},
		handleUploadedFile: function ( e ) {
			const { input } = this.$refs;

			const file = input.files[ 0 ];

			this.$emit( "choose", { file, e } );

			this.isEmpty = false;
		}
	}
}
</script>