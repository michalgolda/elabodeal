<template>
	<number-input-controls
		@incrementValue="handleIncrementValue"
		@decrementValue="handleDecrementValue"
	>
		<div class="price">
			<input
				class="price__input"
				type="number"
				step=".01"
				:class="{ 'form__input-error': price.error }"
				:value="_parseValue( price.value ? price.value : 0 )"
				@change="handleChangeValue"
			/>
			<div class="price__currency">
				PLN
			</div>
		</div>
	</number-input-controls>
</template>
<script>
import { mapState } from "vuex";

import NumberInputControls from "../../../../components/NumberInputControls.vue";

export default {
	computed: mapState( {
		price: state => state.form.fields.price,
		fee: state => state.fee
	} ),
	components: {
		NumberInputControls
	},
	methods: {
		handleChangeValue: function ( e ) {
			const input = e.target;
			const inputValue = Number.parseInt( input.value );

			if ( inputValue <= 0 ) {
				input.value = this._parseValue( 0 );
				
				this.$store.commit(
					"updateFormData",
					{
						fieldName: "price",
						fieldValue: null
					}
				)
			
				return;
			} else if ( inputValue >= 500 ) {
				input.value = this._parseValue( 500 + this.fee );

				this.$store.commit(
					"updateFormData",
					{
						fieldName: "price",
						fieldValue: 500 + this.fee
					}
				)

				return;
			}

			this.$store.commit(
				"updateFormData",
				{
					fieldName: "price",
					fieldValue: inputValue + this.fee
				}
			)
		},
		handleDecrementValue: function ( e ) {
			const value = this.price.value ? this.price.value : 0;

			if ( value <= 0 ) {
				this.$store.commit(
					"updateFormData",
					{
						fieldName: "price",
						fieldValue: null
					}
				);

				return;
			}

			const updatedValue = value - (1 + this.fee);

			this.$store.commit(
				"updateFormData",
				{
					fieldName: "price",
					fieldValue: updatedValue
				}
			);
		},
		handleIncrementValue: function ( e ) {
			const value = this.price.value ? this.price.value : 0;

			if ( value >= 500 )
				return;

			const updatedValue = value + (1 + this.fee);

			this.$store.commit( 
				"updateFormData",
				{
					fieldName: "price",
					fieldValue: updatedValue
				}
			);
		},
		_parseValue: function ( value ) {
			return Number.parseFloat( value ).toFixed( 2 );
		}
	}
}
</script>