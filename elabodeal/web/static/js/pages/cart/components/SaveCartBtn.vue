<template>
	<button 
		v-if="showBtn"
		class="btn btn__primary"
		@click="handleClick"
	>
		Zapisz koszyk
	</button>
</template>
<script>
import { mapState } from 'vuex';


export default {
	computed: mapState({
		showBtn: state => state.products.length > 0
	}),
	methods: {
		handleClick () {
			this.$modalManager.show('saveCartModal');
		}
	}
}
</script>