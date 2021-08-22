<template>
    <div class="wrapper flex-center">
        <div class="section">
            <EndResetPasswordForm v-if="showEndStep" />
            <StartResetPasswordForm v-else />
        </div>
    </div>
</template>
<script>
import { createNamespacedHelpers, mapState as mapRootState } from 'vuex'
import { getUrlParam } from '@/utils/url'

import EndResetPasswordForm from './EndResetPasswordForm'
import StartResetPasswordForm from './StartResetPasswordForm'

const { 
    mapState: mapUiState,
    mapMutations: mapUiMutations } = createNamespacedHelpers('ui');


export default {
    components: {
        EndResetPasswordForm,
        StartResetPasswordForm
    },
    computed: {
        ...mapRootState(['email']),
        ...mapUiState({
            showEndStep (state) {
                return state.step === 'end' && this.email;
            }
        })
    },
    created () {
        const stepParam = getUrlParam('step');

        this.setStep(stepParam);
    },
    methods: mapUiMutations(['setStep'])
}
</script>
