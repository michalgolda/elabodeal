<template>
	<number-input-controls
		@incrementValue="handleIncrementValue"
		@decrementValue="handleDecrementValue"
	>
		<input 
			type="number"
			name="copies"
			:class="{ 'form__input-error': copies.error }"
			:value="copies.value"
			@change="handleChangeValue"
		/>
	</number-input-controls>
</template>
<script>
import { mapState } from "vuex";

import NumberInputControls from "../../../../components/NumberInputControls.vue";

export default {
	computed: mapState( {
		copies: state => state.form.fields.copies
	} ),
	components: {
		NumberInputControls
	},
	methods: {
		handleIncrementValue: function ( e ) {
			const value = this.copies.value ? this.copies.value : 0;

			const updatedValue = value + 1;

			this.$store.commit(
				"updateFormData",
				{
					fieldName: "copies",
					fieldValue: updatedValue
				}
			);
		},
		handleDecrementValue: function ( e ) {
			const value = this.copies.value ? this.copies.value : 0;

			const updatedValue = value - 1;

			if ( updatedValue <= 0 ) {
				this.$store.commit(
					"updateFormData",
					{
						fieldName: "copies",
						fieldValue: null
					}
				)

				return;
			}

			this.$store.commit(
				"updateFormData",
				{
					fieldName: "copies",
					fieldValue: updatedValue
				}
			);
		}
	}
}
</script>