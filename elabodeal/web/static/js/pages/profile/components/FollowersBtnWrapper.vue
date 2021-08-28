<template>
    <UnFollowBtn 
        :publisher-id="publisherId"
        v-if="userAlreadyFollowing"
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

        const userAlreadyFollowing = computed(() => {
            return store.state.userAlreadyFollowing
        })

        return {
            userAlreadyFollowing
        }
    }
}
</script>
