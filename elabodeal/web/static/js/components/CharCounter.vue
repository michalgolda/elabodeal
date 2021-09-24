<template>
    <div>
        <slot :update="updateCharCount" />
        <p class="form__input-remainingCharCount">
            Pozostała ilość znaków: {{ charCount }}
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

        const charCount = ref(maxValue.value - initialValue.value)

        const updateCharCount = (e) => {
            charCount.value = maxValue.value - e.target.value.length
        }

        return {
            charCount,
            updateCharCount
        }        
    }
}
</script>