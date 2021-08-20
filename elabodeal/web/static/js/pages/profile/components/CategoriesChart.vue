<template>
    <Chart 
        title="Kategorie"
        :labels="labels"
        :datasets="datasets"
    />
</template>
<script>
import Chart from './Chart';
import { appData } from '@/utils/data';


export default {
    components: {
        Chart
    },
    data () {
        const { labels, datasets } = appData['charts']['categories'];

        return { labels, datasets };
    }
}
</script>
