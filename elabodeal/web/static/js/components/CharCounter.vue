<template>
    <div>
        <slot :update="updateRemainingCharCount" />
        <p class="form__input-remainingCharCount">
            Pozostała ilość znaków: {{ remainingCharCount }}
        </p>
    </div>
</template>
<script>
import { ref, toRefs } from 'vue'


export default {
    name: 'CharCounter',
    props: {
        maxValue: {
            type: Number,
            required: true
        },
        initialValue: {
            type: Number,
            default: 0
        }
    },
    setup (props) {
        const { maxValue, initialValue } = toRefs(props)

        const remainingCharCount = ref(maxValue.value - initialValue.value)

        const updateRemainingCharCount = (e) => {
            remainingCharCount.value = maxValue.value - e.target.value.length
        }

        return {
            remainingCharCount,
            updateRemainingCharCount
        }        
    }
}
</script>