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
import { mapState } from 'vuex';

import FollowBtn from './FollowBtn';
import UnFollowBtn from './UnFollowBtn';


export default {
    components: {
        FollowBtn,
        UnFollowBtn
    },
    computed: mapState(['userAlreadyFollowing']),
    props: {
        publisherId: {
            type: String,
            required: true
        }
    }
}
</script>
