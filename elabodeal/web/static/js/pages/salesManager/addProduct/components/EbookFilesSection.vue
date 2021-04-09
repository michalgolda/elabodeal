<template>
	<div class="form__group">
		<label>
			PRZEŚLIJ EBOOKA 
			<i class="fas fa-question-circle input-information"></i>
		</label>
		<div class="files files-ebook files__grid files__grid-3">
			<template v-for="type in ['PDF', 'MOBI', 'EPUB']">
				<ebook-file-input :type="type" />
			</template>
		</div>
	</div>
	<div class="form__group">
		<div class="files files-ebook">
			<label 
				style="text-align: center;"
			>
				WERSJA DEMONSTRACYJNA 
				<i class="fas fa-question-circle input-information"></i>
			</label>
			<ebook-file-input type="PDF" />
		</div>
	</div>
</template>
<script>
import EbookFileInput from "./EbookFileInput.vue";


export default {
	components: {
		EbookFileInput
	}
}
</script>