<template>
	<div class="price">
		<button 
			class="btn btn__secondary" 
			type="button"
			@click="handleDecrementValue"
		>
			<i class="fas fa-minus"></i>
		</button>
		<div class="price__container">
			<input 
				class="price__input"  
				type="number"
				step=".01"
				:class="{ 'form__input-error': this.price.error }"
				:value="_parseValue( this.price.value ? this.price.value : 0 )"
				@change="handleChangeValue"
			/>
			<div class="price__currency">
				<p>ZŁ</p>
			</div>
		</div>
		<button 
			class="btn btn__secondary" 
			type="button"
			@click="handleIncrementValue"
		>
			<i class="fas fa-plus"></i>
		</button>
	</div>
</template>
<script>
import { mapState } from "vuex";


export default {
	computed: mapState( {
		price: state => state.form.fields.price
	} ),
	data: function () {
		return {
			fee: 1.25
		}
	},
	methods: {
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
		handleDecrementValue: function ( e ) {
			const value = this.price.value ? this.price.value : 0;

			if ( value <= 0 )
				return;

			const updatedValue = value - (1 + this.fee);

			this.$store.commit(
				"updateFormData",
				{
					fieldName: "price",
					fieldValue: updatedValue
				}
			);
		},
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
		_parseValue: function ( value ) {
			return Number.parseFloat( value ).toFixed( 2 );
		}
	}
}
</script>