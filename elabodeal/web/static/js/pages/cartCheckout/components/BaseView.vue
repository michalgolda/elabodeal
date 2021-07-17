<template>
	<div class="wrapper">
		<Steps />
		<div class="section">
			<slot />
		</div>
	</div>
</template>
<script>
import Steps from './Steps';


export default {
	components: {
		Steps
	}
}
</script>