import { appData } from '@/utils/data'
import { createNamespacedTypes } from '@/utils/store'


const state = () => {
    const { categories, languages } = appData['charts']
    
    return {
        languages,
        categories
    }
}

const getterTypes = {
    GET_LANGUAGES_CHART_DATA: 'GET_LANGUAGES_CHART_DATA',
    GET_CATEGORIES_CHART_DATA: 'GET_CATEGORIES_CHART_DATA'
}

const getters = {
    [getterTypes.GET_CATEGORIES_CHART_DATA] (state) {
        return state.categories
    },
    [getterTypes.GET_LANGUAGES_CHART_DATA] (state) {
        return state.languages
    }
}

export const chartsModuleTypes = createNamespacedTypes('charts', {
    getters: getterTypes
})

const chartsModule = {
    state,
    getters,
    namespaced: true
}

export default chartsModule