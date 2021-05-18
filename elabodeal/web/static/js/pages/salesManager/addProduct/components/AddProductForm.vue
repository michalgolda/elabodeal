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
		<div class="form__group">
			<div>
				<label>CENA</label>
				<div class="flex-center" style="width: 100%;">
					<div>
						<price-input />
					</div>
				</div>
			</div>			
		</div>
		<additional-data-section />
		<consents-section />
		<button class="btn btn__primary">Dodaj produkt</button>
		<button class="btn btn__secondary" type="button">Dodaj wersje językowe</button>
	</form>
</template>
<script>
import { mapState } from "vuex";

import Alert from "../../../../alert";
import publisherService from "../../../../services/publisher";

import StandardDataSection from "./StandardDataSection.vue";
import EbookFilesSection from "./EbookFilesSection.vue";
import AgeCategorySection from "./AgeCategorySection.vue";
import ImagesSection from "./ImagesSection.vue";
import AdditionalDataSection from "./AdditionalDataSection.vue";
import ConsentsSection from "./ConsentsSection.vue";

import PriceInput from "./PriceInput.vue";


export default {
	components: {
		PriceInput,
		ImagesSection,
		ConsentsSection,
		EbookFilesSection,
		AgeCategorySection,
		StandardDataSection,
		AdditionalDataSection
	},
	computed: mapState( [ "form" ] ),
	methods: {
		handleSubmitForm: function ( e ) {
			e.preventDefault();

			this.$store.commit( "validateFormData" );

			if ( !this.form.isValid ) {
				window.scrollTo( 0, 0 );

				Alert.info( "Popraw błędy w formularzu." );

				return;
			}

			const formData = new FormData();
			for ( var key of Object.keys( this.form.fields ) ) {
				const value = this.form.fields[ key ].value;

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
				() => window.location = '/',
				( error ) => {
					const { data } = error.response;

					const fieldNames = Object.keys( data );

					for ( var fieldName of fieldNames ) {
						const field = this.form.fields[ fieldName ];

						field.error = true;

						window.scrollTo( 0, 0 );
					}
				}
			);
		}
	}
}
</script>