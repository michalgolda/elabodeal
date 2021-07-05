<template>
	<number-input-controls
		@incrementValue="handleIncrementValue"
		@decrementValue="handleDecrementValue"
	>
		<input 
			class="copies__input"
			type="number"
			name="copies"
			:class="{ 'form__input-error': copies.error }"
			:value="copies.value"
			@change="handleChangeValue"
			v-if="!showInfinity"
		>
		<span 
			class="copies__input-infinity"
			v-else
		>
			<i class="fas fa-infinity" />
		</span>
	</number-input-controls>
</template>
<script>
import { mapState } from "vuex";

import NumberInputControls from "../../../../components/NumberInputControls.vue";

export default {
	computed: mapState( {
		copies: state => state.form.fields.copies,
		showInfinity: state => state.form.fields.copies.value == 0 ? true : false
	} ),
	components: {
		NumberInputControls
	},
	methods: {
		handleIncrementValue: function () {
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
		handleDecrementValue: function () {
			const value = this.copies.value ? this.copies.value : 0;

			const updatedValue = value - 1;

			if ( updatedValue <= 0 ) {
				this.$store.commit(
					"updateFormData",
					{
						fieldName: "copies",
						fieldValue: 0
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
		},
		handleChangeValue: function ( e ) {
			const input = e.target;
			const inputValue = Number.parseInt( input.value );

			if ( inputValue <= 0 ) {
				this.$store.commit(
					"updateFormData",
					{
						fieldName: "copies",
						fieldValue: 0
					}
				)
			} 
		}
	}
}
</script>