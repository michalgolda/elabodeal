<template>
	<p class="form__group-title">Premiera</p>
	<div class="form__group form__group-grid form__group-grid-2">
		<div>
			<label>DATA</label>
			<input 
				type="date" 
				name="premiere_date"
				:class="{ 'form__input-error': this.form.fields.premiere_datetime.error }"
				@change="handleChangePremiereDate"
			/>
		</div>
		<div>
			<label>GODZINA</label>
			<input
				type="time"
				name="premiere_time"
				:class="{ 'form__input-error': this.form.fields.premiere_datetime.error }"
				:value="this.premiereTime"
				@change="handleChangePremiereTime"
			/>
		</div>
	</div>
</template>
<script>
import { mapState } from "vuex";

export default {
	computed: mapState( [ "form" ] ),
	methods: {
		handleChangePremiereDate: function ( e ) {
			const { value } = e.target;

			this.premiereDate = value;

			if ( this.premiereDate && this.premiereTime ) {
				this.$store.commit(
					"updateFormData",
					{
						fieldName: "premiere_datetime",
						fieldValue: this._prepareDatetimeString()
					}
				)
			}
		},
		handleChangePremiereTime: function ( e ) {
			const { value } = e.target;

			this.premiereTime = value;
			
			if ( this.premiereDate && this.premiereTime ) {
				this.$store.commit(
					"updateFormData",
					{
						fieldName: "premiere_datetime",
						fieldValue: this._prepareDatetimeString()
					}
				)
			}
		},
		_prepareDatetimeString: function () {
			const dateString = `${this.premiereDate} ${this.premiereTime}`;

			return dateString;
		}
	},
	data: function() {
		const currentDate = new Date();
		currentDate.setHours( currentDate.getHours() + 1 );

		const hoursString = `${currentDate.getHours()}`;

		const minutes = currentDate.getMinutes();
		const minutesString = minutes < 10 ? `0${minutes}` : `${minutes}`;

		const defaultTime = `${hoursString}:${minutesString}`;

		return { premiereDate: null, premiereTime: defaultTime };
	}
}
</script>