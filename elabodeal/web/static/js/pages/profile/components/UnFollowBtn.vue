<template>
    <button 
        @click="unfollowPublisherProfile"
        class="btn btn__secondary"
    >
        <i class="fas fa-check" />&nbsp;&nbsp;
        Obserwujesz
    </button>
</template>
<script>
import { toRefs } from 'vue'
import { useStore } from 'vuex'

import {  actionsTypes } from '../store/actions'


export default {
    props: {
        publisherId: {
            type: String,
            required: true
        }
    },
    setup (props) {
        const { publisherId } = toRefs(props)
    
        const store = useStore()

        const unfollowPublisherProfile = () => {
            store.dispatch(
                actionsTypes.UNFOLLOW_PUBLISHER_PROFILE,
                { publisherId: publisherId.value }
            )
        }

        return {
            unfollowPublisherProfile
        }
    }
}
</script>
