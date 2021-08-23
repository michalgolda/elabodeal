<template>
    <div class="wrapper flex-center">
        <div class="section">
            <EndResetPasswordForm v-if="showEndForm" />
            <StartResetPasswordForm v-else />
        </div>
    </div>
</template>
<script>
import { computed } from 'vue'
import { useStore } from 'vuex'

import { mainModuleTypes, uiModuleTypes } from '../store/modules'
import { getUrlParam } from '@/utils/url'

import EndResetPasswordForm from './EndResetPasswordForm'
import StartResetPasswordForm from './StartResetPasswordForm'


export default {
    components: {
        EndResetPasswordForm,
        StartResetPasswordForm
    },
    setup () {
        const store = useStore()

        const stepParam = getUrlParam('step')
        const emailParam = getUrlParam('email')

        store.commit(
            uiModuleTypes.mutations.SET_STEP,
            stepParam
        )

        store.commit(
            mainModuleTypes.mutations.SET_EMAIL,
            emailParam
        )

        const showEndForm = computed(() => {
            return store.getters[uiModuleTypes.getters.SHOW_END_FORM]
        })

        return {
            showEndForm
        }
    }
}
</script>
