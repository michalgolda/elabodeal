<template>
    <button 
        @click="handleClick"
        class="btn btn__secondary"
    >
        <i class="fas fa-check" />&nbsp;&nbsp;
        Obserwujesz
    </button>
</template>
<script>
import { mapActions } from 'vuex';


export default {
    props: {
        publisherId: {
            type: String,
            required: true
        }
    },
    methods: {
        ...mapActions(['unFollowPublisherProfile']),
        handleClick () {
            this.unFollowPublisherProfile({
                publisherId: this.publisherId
            });
        }
    }
}
</script>
