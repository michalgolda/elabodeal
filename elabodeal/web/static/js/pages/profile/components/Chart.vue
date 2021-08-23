<template>
    <div ref="chartContainerRef" />
</template>
<script>
import { ref, onMounted } from 'vue'


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
        // eslint-disable-next-line
        const { labels, datasets, title } = props;

        const config = {
            type: 'doughnut',
            data: {
                labels: labels,
                datasets: datasets,
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
                        text: title,
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

            const canvas = document.createElement('canvas');

            chartContainer.appendChild(canvas);

            // eslint-disable-next-line
            new Chart(canvas, config);
        })

        return {
            chartContainerRef
        }
    }
}
</script>