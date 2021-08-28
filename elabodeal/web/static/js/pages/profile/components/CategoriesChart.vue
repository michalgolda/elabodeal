<template>
    <Chart 
        title="Kategorie"
        :labels="labels"
        :datasets="datasets"
    />
</template>
<script>
import { computed } from 'vue'
import { useStore } from 'vuex'

import Chart from './Chart';


export default {
    components: {
        Chart
    },
    setup () {
        const store = useStore()

        const chartData = store.state.charts.categories

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
