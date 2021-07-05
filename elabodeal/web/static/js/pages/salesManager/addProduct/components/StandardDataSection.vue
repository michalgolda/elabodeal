<template>
	<div class="form__group form__group-grid form__group-grid-2">
		<div>
			<label>KATEGORIA</label>
			<select 
				name="category"
				:class="{ 'form__input-error': this.form.fields.category_id.error }"
				@change="handleChangeCategory"
			>
				<option 
					selected 
					disabled
				>
					Wybierz kategorie
				</option>
				<option
					v-for="category in categories"
					:key="category.id"
				>
					{{ category.name }}
				</option>
			</select>
		</div>
		<div>
			<label>JĘZYK</label>
			<select 
				name="language"
				:class="{ 'form__input-error': this.form.fields.product_language_id.error }"
				@change="handleChangeLanguage"
			>
				<option 
					selected 
					disabled
				>
					Wybierz język
				</option>
				<option
					v-for="language in supportedLanguages"
					:key="language.id"
				>
					{{ language.name }}
				</option>
			</select>
		</div>
	</div>
	<div class="form__group form__group-grid form__group-grid-3">
		<div>
			<label>ILOŚĆ STRON</label>
			<page-count-input />
		</div>
		<div>
			<label>ROK WYDANIA</label>
			<published-year-input />
		</div>
		<div>
			<label>LICZBA KOPII</label>
			<copies-input />
		</div>
	</div>
	<div class="form__group">
		<label>TYTUŁ</label>
		<input 
			type="text" 
			name="title"
			:class="{ 'form__input-error': this.form.fields.title.error }"
			@change="handleChangeTitle"
			@keyup="this.$store.commit('clearFieldError', { fieldName: 'title' })"
		>
	</div>
	<div class="form__group">
		<label>AUTOR</label>
		<input 
			type="text" 
			name="author"
			:class="{ 'form__input-error': this.form.fields.author.error }"
			@change="handleChangeAuthor"
			@keyup="this.$store.commit('clearFieldError', { fieldName: 'author' })"
		>
	</div>
	<div class="form__group form__group-textarea">
		<label>
			OPIS 
			<i class="fas fa-question-circle input-information" />
		</label>
		<textarea
			name="description"
			:class="{ 'form__input-error': this.form.fields.description.error }"
			@change="handleChangeDescription"
			@keyup="this.$store.commit( 'clearFieldError', { fieldName: 'description' } )"
		/>
		<p>Pozostało znaków: 9000</p>
	</div>
	<div class="form__group form__group-textarea">
		<label>SPIS TREŚCI</label>
		<textarea 
			name="contents"
			@change="handleChangeContents"
		/>
		<p>Pozostało znaków: 9000</p>
	</div>
	<div class="form__group">
		<label>
			NUMER ISBN 
			<i class="fas fa-question-circle input-information" />
		</label>
		<input
			type="text" 
			name="isbn"
			:class="{ 'form__input-error': this.form.fields.isbn.error }"
			@change="handleChangeIsbn"
			@keyup="this.$store.commit('clearFieldError', {fieldName: 'isbn'})"
		>
	</div>
</template>
<script>
import { mapState } from "vuex";

import CopiesInput from "./CopiesInput.vue";
import PageCountInput from "./PageCountInput.vue";
import PublishedYearInput from "./PublishedYearInput.vue";


export default {
	components: {
		CopiesInput,
		PageCountInput,
		PublishedYearInput
	},
	computed: mapState( [ "categories", "supportedLanguages", "form" ] ),
	methods: {
		handleChangeCategory: function ( e ) {
			const { value } = e.target;

			this.$store.commit(
				"updateFormData",
				{
					fieldName: "category_id",
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
					fieldName: "product_language_id",
					fieldValue: this.supportedLanguages.find(
						( language ) => language.name === value
					).id
				}
			)
		},
		handleChangeAuthor: function ( e ) {
			const { value } = e.target;

			this.$store.commit(
				"updateFormData",
				{
					fieldName: "author",
					fieldValue: value
				}
			)
		},
		handleChangeTitle: function ( e ) {
			const { value } = e.target;

			this.$store.commit(
				"updateFormData",
				{
					fieldName: "title",
					fieldValue: value
				}
			)
		},
		handleChangeDescription: function ( e ) {
			const { value } = e.target;

			this.$store.commit(
				"updateFormData",
				{
					fieldName: "description",
					fieldValue: value
				}
			)
		},
		handleChangeContents: function ( e ) {
			const { value } = e.target;

			this.$store.commit(
				"updateFormData",
				{
					fieldName: "contents",
					fieldValue: value
				}
			)
		},
		handleChangeIsbn: function ( e ) {
			const { value } = e.target;

			this.$store.commit(
				"updateFormData",
				{
					fieldName: "isbn",
					fieldValue: value
				}
			)
		}
	}
}
</script>