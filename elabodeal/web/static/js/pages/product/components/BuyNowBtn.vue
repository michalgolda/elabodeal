<template>
    <button
        @click="buyNowProduct"
        class="btn btn__primary"
    >
        Kup teraz
    </button>
</template>
<script>
import { toRefs } from 'vue'
import { useStore } from 'vuex'

import { actionsTypes } from '../store/actions'


export default {
    props: {
        productId: {
            type: String,
            required: true
        }
    },
    setup (props) {
        const { productId } = toRefs(props)

        const store = useStore()

        const buyNowProduct = () => {
            store.dispatch(
                actionsTypes.BUY_NOW_PRODUCT,
                { productId: productId.value }
            )
        }

        return { buyNowProduct }
    }
}
</script>