<template>
    <UnFollowBtn 
        :publisher-id="publisherId"
        v-if="currentUserAlreadyFollowing"
    />
    <FollowBtn 
        :publisher-id="publisherId"
        v-else
    />
</template>
<script>
import { computed } from 'vue'
import { useStore } from 'vuex'

import FollowBtn from './FollowBtn'
import UnFollowBtn from './UnFollowBtn'


export default {
    components: {
        FollowBtn,
        UnFollowBtn
    },
    props: {
        publisherId: {
            type: String,
            required: true
        }
    },
    setup () {
        const store = useStore()

        const currentUserAlreadyFollowing = computed(() => {
            return store.state.currentUserAlreadyFollowing
        })

        return {
            currentUserAlreadyFollowing
        }
    }
}
</script>
