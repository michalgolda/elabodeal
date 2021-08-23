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
import { mainModuleTypes } from '../store/modules'

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
    setup (props) {
        const { publisherId } = props
        
        const store = useStore()

        const userAlreadyFollowing = computed(() => {
            return store.getters[mainModuleTypes.getters.GET_USER_ALREADY_FOLLOWING]
        })

        return {
            publisherId,
            userAlreadyFollowing
        }
    }
}
</script>
