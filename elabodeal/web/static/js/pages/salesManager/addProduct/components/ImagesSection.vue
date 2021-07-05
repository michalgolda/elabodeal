<template>
	<div class="form__group">
		<label>OKŁADKA</label>
		<p 
			class="error-text" 
			v-if="this.form.fields.cover_img.error"
		>
			Okładka jest obowiązkowa
		</p>
		<div class="files files-image files-image-cover">
			<image-file-input :is-cover="true" />
			<p class="form__group-details form__group-details-cover">
				ajwdjhajwdhajwdhajwdhajwhdjawhdajwdhajwdhajwdhawjdhajwdhajwdhajwdhajwdhawjdhawjdhajwdhajwdh
			</p>
		</div>
	</div>
	<div class="form__group">
		<label>DODATKOWE ZDJĘCIA</label>
		<p class="form__group-details">
			ajwdjhajwdhajwdhajwdhajwhdjawhdajwdhajwdhajwdhawjdhajwdhajwdhajwdhajwdhawjdhawjdhajwdhajwdh
		</p>
		<div class="files files-image files__grid files__grid-4">
			<image-file-input 
				v-for="index in 8"
				:key="index"
			/>
		</div>
	</div>
</template>
<script>
import { mapState } from "vuex";
import ImageFileInput from "./ImageFileInput.vue";


export default {
	components: {
		ImageFileInput
	},
	computed: mapState( [ "form" ] )
}
</script>