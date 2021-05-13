<template>
	<div>
		<label>DATA PREMIERY</label>
		<input 
			type="date" 
			name="premiere_date"
			@change="handleChangePremiereDate"
		/>
	</div>
</template>
<script>
export default {
	methods: {
		handleChangePremiereDate: function ( e ) {
			const { value } = e.target;

			this.$store.commit(
				"updateFormData",
				{
					fieldName: "premiere_date",
					fieldValue: value
				}
			)
		}
	}
}
</script>