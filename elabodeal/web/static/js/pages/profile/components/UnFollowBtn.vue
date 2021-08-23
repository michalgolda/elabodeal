<template>
    <button 
        @click="unFollowPublisherProfile"
        class="btn btn__secondary"
    >
        <i class="fas fa-check" />&nbsp;&nbsp;
        Obserwujesz
    </button>
</template>
<script>
import { useStore } from 'vuex'
import {  mainModuleTypes } from '../store/modules'


export default {
    props: {
        publisherId: {
            type: String,
            required: true
        }
    },
    setup (props) {
        const { publisherId } = props
    
        const store = useStore()

        const unFollowPublisherProfile = () => {
            store.dispatch(
                mainModuleTypes.actions.UNFOLLOW_PUBLISHER_PROFILE,
                { publisherId }
            )
        }

        return {
            unFollowPublisherProfile
        }
    }
}
</script>
