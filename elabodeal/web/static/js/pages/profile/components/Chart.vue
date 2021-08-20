<template>
    <div ref="chartContainer" />
</template>
<script>
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
    data () {
        return {
            config: {
                type: 'doughnut',
                data: {
                    labels: this.labels,
                    datasets: this.datasets,
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
                            text: this.title,
                            padding: {
                                bottom: 10
                            }
                        }
                    }
                }
            }
        }
    },
    mounted () {
        const chartContainer = this.$refs['chartContainer'];
        
        const canvas = document.createElement('canvas');

        chartContainer.appendChild(canvas);

        // eslint-disable-next-line
        this.chart = new Chart(canvas, this.config);
    }
}
</script>