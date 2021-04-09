<template>
	<div class="form__group">
		<label>
			KATEGORIA WIEKOWA 
			<i class="fas fa-question-circle input-information"></i>
		</label>
		<div class="age-categories">
			<template v-for="age in [ 3, 7, 12, 16, 18 ]">
				<div
					class="age-category"
					:age="age"
					:class="{ 'age-category-selected': selectedAgeCategory === age }"
					@click="handleChangeAgeCategory"
				>
					<p>+{{ age }}</p>
				</div>
			</template>
		</div>
	</div>
</template>
<script>
export default {
	data: function() {
		return {
			selectedAgeCategory: 3
		}
	},
	methods: {
		handleChangeAgeCategory: function ( e ) {
			const value = Number(e.target.getAttribute( 'age' ));

			this.selectedAgeCategory = value;

			this.$store.commit(
				'updateFormData',
				{
					fieldName: 'age_category',
					fieldValue: value
				}
			)
		}
	}
}
</script>