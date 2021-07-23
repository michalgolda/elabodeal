<template>
    <button
        @click="handleClick"
        class="btn btn__primary"
    >
        Kup teraz
    </button>
</template>
<script>
import { mapActions } from 'vuex';


export default {
    props: {
        productId: {
            type: String,
            required: true
        }
    },
    methods: {
        ...mapActions(['buyNowProduct']),
        handleClick () {
            this.buyNowProduct({
                productId: this.productId
            });
        }
    }
}
</script>