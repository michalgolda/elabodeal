<template>
	<Chart 
		title="Języki"
		:labels="labels"
		:datasets="datasets"
	/>
</template>
<script>
import { computed } from 'vue'
import { useStore } from 'vuex'

import Chart from './Chart'


export default {
	components: {
		Chart
	},
	setup () {
		const store = useStore()

		const chartData = store.state.charts.languages

		const labels = computed(() => {
			return chartData['labels']
		})

		const datasets = computed(() => {
			return chartData['datasets']
		})

		return {
			labels,
			datasets
		}
	}
}
</script>