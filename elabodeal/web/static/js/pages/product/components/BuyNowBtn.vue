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
import { cartModuleTypes } from '../store/modules'


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
                cartModuleTypes.actions.BUY_NOW_PRODUCT,
                { productId: productId.value }
            )
        }

        return { buyNowProduct }
    }
}
</script>