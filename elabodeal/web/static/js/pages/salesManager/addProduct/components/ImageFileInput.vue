<template>
	<file-input 
		accept=".jpg,.png"
		v-slot="input"
		@choose="handleChooseFile"
		@delete="handleDeleteFile"
	>
		<div 
			class="file"
		>
			<div 
				class="file__upload"
				:class="{ 'file__upload-cover': isCover }"
				@click="input.handleChooseFile"
				v-show="input.isEmpty"
			>
				<i class="fas fa-image"></i>
			</div>
			<div 
				class="file__upload file__upload-preview"
				:class="{ 'file__upload-cover': isCover }"
				v-show="!input.isEmpty"
			>
				<img ref="imagePreview" />
				<div class="file__upload-actions">
					<button 
						class="btn btn__danger" 
						type="button"
						@click="input.handleDeleteFile"
					>
						<i class="fas fa-trash-alt"></i>
					</button>
				</div>
			</div>
		</div>
	</file-input>
</template>
<script>
import { mapState } from "vuex";
import FileInput from "./FileInput.vue";


export default {
	components: {
		FileInput
	},
	props: {
		isCover: {
			default: false,
			type: Boolean
		}
	},
	computed: mapState( [ "formData" ] ),
	methods: {
		handleChooseFile: function ( { file, e } ) {
			const { imagePreview } = this.$refs;

			const reader = new FileReader();

			reader.onload = function() {
				imagePreview.src = reader.result;
			}
			reader.readAsDataURL( file );

			var value;

			file.id = String( Math.random() );

			if ( this.isCover ) {
				value = file;
			} else { 
				value = this.formData[ 'other_images' ];
				value.push( file );
			}

			this.$store.commit(
				'updateFormData',
				{
					fieldName: this.isCover ? 'cover_img' : 'other_images',
					fieldValue: value
				}
			)
		},
		handleDeleteFile: function ( { file, e } ) {
			const { imagePreview } = this.$refs;

			imagePreview.src = '';

			var value;

			if ( this.isCover ) {
				value = null;
			} else {
				value = this.form.data[ 'other_images' ].filter(
					( element ) => element.id !== file.id
				)
			}

			this.$store.commit(
				'updateFormData',
				{
					fieldName: this.isCover ? 'cover_img' : 'other_images',
					fieldValue: value
				}
			)
		}
	}
}
</script>