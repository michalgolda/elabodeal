<template>
	<div class="wrapper">
		<Steps />
		<div class="wrapper wrapper-content">
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