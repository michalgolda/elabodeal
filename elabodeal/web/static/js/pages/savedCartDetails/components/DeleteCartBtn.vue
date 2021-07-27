<template>
    <button
        @click="handleClick" 
        class="btn btn__danger"
    >
        Usuń
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
        ...mapActions(['deleteCart']),
        handleClick () {
            this.deleteCart({
                cartId: this.cartId
            });
        }
    }
}
</script>