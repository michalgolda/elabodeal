<template>
	<div class="number-input-controls">
		<button 
			class="btn btn__secondary" 
			type="button"
			@click="$emit( 'decrementValue' )"
		>
			<i class="fas fa-minus"></i>
		</button>
		<div class="input-wrapper">
			<slot />
		</div>
		<button 
			class="btn btn__secondary" 
			type="button"
			@click="$emit( 'incrementValue' )"
		>
			<i class="fas fa-plus"></i>
		</button>
	</div>
</template>
<script>
export default {
	emits: [ "incrementValue", "decrementValue" ]
}
</script>