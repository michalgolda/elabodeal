<template>
	<form 
		class="form" 
		autocomplete="off"
		@submit="handleSubmitForm" 
	>
		<standard-data-section />
		<ebook-files-section />
		<age-category-section />
		<images-section />
		<consents-section />
		<button class="btn btn__primary">Dodaj produkt</button>
		<button class="btn btn__secondary" type="button">Dodaj wersje językowe</button>
	</form>
</template>
<script>
import { mapState } from "vuex";

import publisherService from "../../../../services/publisher";

import StandardDataSection from "./StandardDataSection.vue";
import EbookFilesSection from "./EbookFilesSection.vue";
import AgeCategorySection from "./AgeCategorySection.vue";
import ImagesSection from "./ImagesSection.vue";
import ConsentsSection from "./ConsentsSection.vue";


export default {
	components: {
		StandardDataSection,
		AgeCategorySection,
		EbookFilesSection,
		ImagesSection,
		ConsentsSection
	},
	computed: mapState( [ "formData" ] ),
	methods: {
		handleSubmitForm: function ( e ) {
			e.preventDefault();

			const formData = new FormData();
			for ( var key of Object.keys( this.formData ) ) {
				const value = this.formData[ key ];

				if ( key === "files" || key === "other_images" ) {
					value.forEach(
						( file ) => formData.append( key, file )
					)
				} else {
					formData.append( key, value );
				}
			}

			publisherService.createProduct( 
				'/api/me/products/', 
				formData,
				successHandler = () => window.locaton = '/'
			);
		}
	}
}
</script>