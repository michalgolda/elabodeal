<template>
    <div ref="chartContainerRef" />
</template>
<script>
import { ref, toRefs, onMounted } from 'vue'


export default {
    props: {
        title: {
            type: String,
            required: true
        },
        labels: {
            type: Array,
            required: true
        },
        datasets: {
            type: Array,
            required: true
        }
    },
    setup (props) {
        const { labels, datasets, title } = toRefs(props)

        const config = {
            type: 'doughnut',
            data: {
                labels: labels.value,
                datasets: datasets.value,
            },
            options: {
                plugins: {
                    legend: {
                        labels: {
                            boxWidth: 10,
                            boxHeight: 10
                        },
                        position: 'bottom'
                    },
                    title: {
                        display: true,
                        text: title.value,
                        padding: {
                            bottom: 10
                        }
                    }
                }
            }
        }

        const chartContainerRef = ref(null)

        onMounted(() => {
            const chartContainer = chartContainerRef.value

            const canvas = document.createElement('canvas')

            chartContainer.appendChild(canvas)

            // eslint-disable-next-line
            new Chart(canvas, config)
        })

        return {
            chartContainerRef
        }
    }
}
</script>