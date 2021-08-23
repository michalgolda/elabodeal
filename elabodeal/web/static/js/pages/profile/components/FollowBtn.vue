<template>
    <button 
        @click="followPublisherProfile"
        class="btn btn__primary"
    >
        Zaobserwuj
    </button>
</template>
<script>
import { useStore } from 'vuex'
import { mainModuleTypes } from '../store/modules'


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

        const followPublisherProfile = () => {
            store.dispatch(
                mainModuleTypes.actions.FOLLOW_PUBLISHER_PROFILE,
                { publisherId }
            )
        }

        return {
            followPublisherProfile
        }
    }
}
</script>
