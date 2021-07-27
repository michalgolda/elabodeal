<template>
    <button 
        @click="handleClick"
        class="btn btn__secondary"
    >
        Udostępnij
    </button>
</template>
<script>
import { mapActions } from 'vuex';


export default {
    props: {
        cartId: {
            type: String,
            required: true
        }
    },
    methods: {
        ...mapActions(['shareCart']),
        handleClick () {
            this.shareCart({
                cartId: this.cartId
            });
        }
    }
}
</script>
