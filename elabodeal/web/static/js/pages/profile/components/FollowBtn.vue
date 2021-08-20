<template>
    <button 
        @click="handleClick"
        class="btn btn__primary"
    >
        Zaobserwuj
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
        ...mapActions(['followPublisherProfile']),
        handleClick () {
            this.followPublisherProfile({
                publisherId: this.publisherId
            });
        }
    }
}
</script>
