<template>
    <p 
        class="form__input-error-msg"
        v-for="error in errors"
        :key="error"
    >
        {{ error }}
    </p>
    <slot :isErrors="isErrors" />
</template>
<script>
import { toRefs, reactive } from 'vue'


export default {
    name: 'InputErrorsWrapper',
    props: {
        errors: {
            type: Array,
            default: () => []
        }
    },
    setup (props) {
        const { errors } = toRefs(props)

        const state = reactive({ isErrors: errors.value.length > 0 })

        return { ...toRefs(state) }
    }
}
</script>