<template>
	<number-input-controls
		@incrementValue="handleIncrementValue"
		@decrementValue="handleDecrementValue"
	>
		<input 
			type="number"
			name="published_year"
			:class="{ 'form__input-error': published_year.error }"
			:value="published_year.value"
			@change="handleChangeValue"
			@keyup="$store.commit( 'clearFieldError', { fieldName: 'published_year' } )"
		>
	</number-input-controls>
</template>
<script>
import { mapState } from "vuex";

import NumberInputControls from "../../../../components/NumberInputControls.vue";

export default {
	computed: mapState( {
		published_year: state => state.form.fields.published_year
	} ),
	components: {
		NumberInputControls
	},
	methods: {
		handleIncrementValue: function () {
			const value = this.published_year.value ? this.published_year.value : 0;
			const updatedValue = value + 1;

			this.$store.commit(
				"updateFormData",
				{
					fieldName: "published_year",
					fieldValue: updatedValue
				}
			);
		},
		handleDecrementValue: function () {
			const value = this.published_year.value ? this.published_year.value : 0;
			const updatedValue = value - 1;

			this.$store.commit(
				"updateFormData",
				{
					fieldName: "published_year",
					fieldValue: updatedValue
				}
			);
		},
		handleChangeValue: function ( e ) {
			const input = e.target;
			const inputValue = Number.parseInt( input.value );

			this.$store.commit(
				"updateFormData",
				{
					fieldName: "published_year",
					fieldValue: inputValue
				}
			);
		}
	}
}
</script>