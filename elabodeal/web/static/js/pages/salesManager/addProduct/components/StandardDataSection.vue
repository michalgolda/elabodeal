<template>
	<div class="form__group form__group-grid form__group-grid-2">
		<div>
			<label>KATEGORIA</label>
			<select 
				name="category"
				@change="handleChangeCategory" 
			>
				<option selected disabled>Wybierz kategorie</option>
				<template v-for="category in categories">
					<option>{{ category.name }}</option>
				</template>
			</select>
		</div>
		<div>
			<label>JĘZYK</label>
			<select 
				name="language"
				@change="handleChangeLanguage"
			>
				<option selected disabled>Wybierz język</option>
				<template v-for="language in supportedLanguages">
					<option>{{ language.name }}</option>
				</template>
			</select>
		</div>
	</div>
	<div class="form__group form__group-grid form__group-grid-3">
		<div>
			<label>ILOŚĆ STRON</label>
			<input 
				type="number" 
				name="page_count"
				required 
				@change="handleChangePageCount"
			/>
		</div>
		<div>
			<label>ROK WYDANIA</label>
			<input 
				type="number" 
				name="published_year" 
				required 
				@change="handleChangePublishedYear"
			/>
		</div>
		<div>
			<label>CENA</label>
			<input 
				type="number" 
				name="price"
				min="0.00" 
				max="1000.00" 
				step="0.01"
				required 
				@change="handleChangePrice"
			/>
		</div>
	</div>
	<div class="form__group">
		<label>TYTUŁ</label>
		<input 
			type="text" 
			name="title"
			required 
			@change="handleChangeTitle"
		/>
	</div>
	<div class="form__group">
		<label>AUTOR</label>
		<input 
			type="text" 
			name="author"
			required
			@change="handleChangeAuthor"
		/>
	</div>
	<div class="form__group form__group-textarea">
		<label>OPIS <i class="fas fa-question-circle input-information"></i></label>
		<textarea
			name="description"
			required 
			@change="handleChangeDescription"
		>
		</textarea>
		<p>Pozostało znaków: 9000</p>
	</div>
	<div class="form__group form__group-textarea">
		<label>SPIS TREŚCI</label>
		<textarea 
			name="contents"
			required 
			@change="handleChangeContents"
		>
		</textarea>
		<p>Pozostało znaków: 9000</p>
	</div>
	<div class="form__group">
		<label>NUMER ISBN <i class="fas fa-question-circle input-information"></i></label>
		<input
			 type="text" 
			 name="isbn"
			 required 
			 @change="handleChangeIsbn"
		/>
	</div>
</template>
<script>
import { mapState } from "vuex";


export default {
	computed: mapState( [ 'categories', 'supportedLanguages' ] ),
	methods: {
		handleChangeCategory: function ( e ) {
			const { value } = e.target;

			this.$store.commit(
				"updateFormData",
				{
					fieldName: 'category_id',
					fieldValue: this.categories.find(
						( category ) => category.name === value
					).id
				}
			)
		},
		handleChangeLanguage: function ( e ) {
			const { value } = e.target;

			this.$store.commit(
				"updateFormData",
				{
					fieldName: 'product_language_id',
					fieldValue: this.supportedLanguages.find(
						( language ) => language.name === value
					).id
				}
			)
		},
		handleChangePageCount: function ( e ) {
			const { value } = e.target;

			this.$store.commit(
				"updateFormData",
				{
					fieldName: 'page_count',
					fieldValue: value
				}
			)
		},
		handleChangePublishedYear: function ( e ) {
			const { value } = e.target;

			this.$store.commit(
				"updateFormData",
				{
					fieldName: 'published_year',
					fieldValue: value
				}
			)
		},
		handleChangePrice: function ( e ) {
			const { value } = e.target;

			this.$store.commit(
				"updateFormData",
				{
					fieldName: 'price',
					fieldValue: value
				}
			)
		},
		handleChangeAuthor: function ( e ) {
			const { value } = e.target;

			this.$store.commit(
				"updateFormData",
				{
					fieldName: 'author',
					fieldValue: value
				}
			)
		},
		handleChangeTitle: function ( e ) {
			const { value } = e.target;

			this.$store.commit(
				"updateFormData",
				{
					fieldName: 'title',
					fieldValue: value
				}
			)
		},
		handleChangeDescription: function ( e ) {
			const { value } = e.target;

			this.$store.commit(
				"updateFormData",
				{
					fieldName: 'description',
					fieldValue: value
				}
			)
		},
		handleChangeContents: function ( e ) {
			const { value } = e.target;

			this.$store.commit(
				"updateFormData",
				{
					fieldName: 'contents',
					fieldValue: value
				}
			)
		},
		handleChangeIsbn: function ( e ) {
			const { value } = e.target;

			this.$store.commit(
				"updateFormData",
				{
					fieldName: 'isbn',
					fieldValue: value
				}
			)
		}
	}
}
</script>