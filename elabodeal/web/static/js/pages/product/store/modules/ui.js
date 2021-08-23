import { createNamespacedTypes } from '@/utils/store'
 

const state = () => {
    return {
        showContents: false,
        showDescription: true
    }
}

const mutationTypes = {
    SHOW_CONTENTS: 'SHOW_CONTENTS',
    SHOW_DESCRIPTION: 'SHOW_DESCRIPTION'
}

const mutations = {
    [mutationTypes.SHOW_CONTENTS] (state) {
        state.showContents = true
        state.showDescription = false
    },
    [mutationTypes.SHOW_DESCRIPTION] (state) {
        state.showContents = false
        state.showDescription = true
    }
}

const getterTypes = {
    SHOW_CONTENTS: 'SHOW_CONTENTS',
    SHOW_DESCRIPTION: 'SHOW_DESCRIPTION'
}

const getters = {
    [getterTypes.SHOW_CONTENTS] (state) {
        return state.showContents
    },
    [getterTypes.SHOW_DESCRIPTION] (state) {
        return state.showDescription
    }
}

export const uiModuleTypes = createNamespacedTypes('ui', {
    getters: getterTypes,
    mutations: mutationTypes
})

const uiModule = {
    state,
    getters,
    mutations,
    namespaced: true
}

export default uiModule