<template>
	<number-input-controls
		@incrementValue="handleIncrementValue"
		@decrementValue="handleDecrementValue"
	>
		<input 
			type="number"
			name="page_count"
			:class="{ 'form__input-error': page_count.error }"
			:value="page_count.value"
			@change="handleChangeValue"
			@keyup="$store.commit( 'clearFieldError', { fieldName: 'page_count' } )"
		/>
	</number-input-controls>
</template>
<script>
import { mapState } from "vuex";

import NumberInputControls from "../../../../components/NumberInputControls.vue";

export default {
	computed: mapState( {
		page_count: state => state.form.fields.page_count
	} ),
	components: {
		NumberInputControls
	},
	methods: {
		handleIncrementValue: function ( e ) {
			const value = this.page_count.value ? this.page_count.value : 0;

			const updatedValue = value + 1;

			this.$store.commit(
				"updateFormData",
				{
					fieldName: "page_count",
					fieldValue: updatedValue
				}
			);
		},
		handleDecrementValue: function ( e ) {
			const value = this.page_count.value ? this.page_count.value : 0;

			const updatedValue = value - 1;

			if ( updatedValue <= 0 ) {
				this.$store.commit(
					"updateFormData",
					{
						fieldName: "page_count",
						fieldValue: 1
					}
				);

				return;
			}

			this.$store.commit(
				"updateFormData",
				{
					fieldName: "page_count",
					fieldValue: updatedValue
				}
			);
		},
		handleChangeValue: function ( e ) {
			const input = e.target;
			const inputValue = Number.parseInt( input.value );

			if ( inputValue <= 0 ) {
				this.$store.commit(
					"updateFormData",
					{
						fieldName: "page_count",
						fieldValue: 1
					}
				);

				return;
			}

			this.$store.commit(
				"updateFormData",
				{
					fieldName: "page_count",
					fieldValue: inputValue
				}
			);
		}
	}
}
</script>