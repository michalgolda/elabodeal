<template>
	<div class="form__group">
		<label>OKŁADKA</label>
		<div class="files files-image files-image-cover">
			<image-file-input :isCover=true />
			<p class="form__group-details form__group-details-cover">ajwdjhajwdhajwdhajwdhajwhdjawhdajwdhajwdhajwdhawjdhajwdhajwdhajwdhajwdhawjdhawjdhajwdhajwdh</p>
		</div>
	</div>
	<div class="form__group">
		<label>DODATKOWE ZDJĘCIA</label>
		<p class="form__group-details">ajwdjhajwdhajwdhajwdhajwhdjawhdajwdhajwdhajwdhawjdhajwdhajwdhajwdhajwdhawjdhawjdhajwdhajwdh</p>
		<div class="files files-image files__grid files__grid-4">
			<template v-for="index in 8">
				<image-file-input />
			</template>
		</div>
	</div>
</template>
<script>
import ImageFileInput from "./ImageFileInput.vue";


export default {
	components: {
		ImageFileInput
	}
}
</script>