<template>
    <button 
        @click="followPublisherProfile"
        class="btn btn__primary"
    >
        Zaobserwuj
    </button>
</template>
<script>
import { toRefs } from 'vue'
import { useStore } from 'vuex'

import { actionsTypes } from '../store/actions'


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

        const followPublisherProfile = () => {
            store.dispatch(
                actionsTypes.FOLLOW_PUBLISHER_PROFILE,
                { publisherId: publisherId.value }
            )
        }

        return {
            followPublisherProfile
        }
    }
}
</script>
