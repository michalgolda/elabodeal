<template>
	<div
		class="file" 
		style="width: 168px; margin: 0 auto;"
	>
		<p class="file__upload-type">{{ type }}</p>
		<file-input 
			v-slot="input"
			:accept="'.' + type.toLocaleLowerCase()"
			@choose="handleChooseFile"
			@delete="handleDeleteFile"
		>
			<template v-if="input.isEmpty">
				<button 
					class="btn btn__secondary btn-block"
					type="button"
					@click="input.handleChooseFile"
				>
					Prześlij
				</button>
			</template>
			<template v-else>
				<button 
					class="btn btn__danger btn-block" 
					type="button"
					@click="input.handleDeleteFile"
				>
					Usuń plik
				</button>
			</template>
		</file-input>
	</div>
</template>
<script>
import { mapState } from "vuex";
import FileInput from "./FileInput.vue";


export default {
	props: {
		type: String
	},
	components: {
		FileInput
	},
	computed: mapState( [ "form" ] ),
	methods: {
		handleChooseFile: function ( { file, e } ) {
			var value = this.form.fields[ "files" ].value;

			file.id = String( Math.random() );

			value.push( file );

			this.$store.commit(
				"updateFormData",
				{
					fieldName: "files",
					fieldValue: value
				}
			)
		},
		handleDeleteFile: function( { file, e } ) {
			var value = this.form.fields[ "files" ].value.filter(
				( element ) => element.id !== file.id
			)

			this.$store.commit(
				"updateFormData",
				{
					fieldName: "files",
					fieldValue: value
				}
			)
		}	
	}
}
</script>