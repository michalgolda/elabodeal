<template>
	<div class="number-input-controls">
		<button 
			class="btn btn__secondary" 
			type="button"
			@click="$emit( 'decrementValue' )"
		>
			<i class="fas fa-minus" />
		</button>
		<div class="input-wrapper">
			<slot />
		</div>
		<button 
			class="btn btn__secondary" 
			type="button"
			@click="$emit( 'incrementValue' )"
		>
		<i class="fas fa-plus" />
		</button>
	</div>
</template>
<script>
export default {
	emits: [ "incrementValue", "decrementValue" ]
}
</script>