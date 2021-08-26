import { getApplicationData } from '@/utils/data'
import { publisherService } from '@/services'
import { createNamespacedTypes } from '@/utils/store'


const state = () => {
    const { userAlreadyFollowing } = getApplicationData()

    return { userAlreadyFollowing }
}

const mutationTypes = {
    INCREMENT_FOLLOWERS_COUNT: 'INCREMENT_FOLLOWERS_COUNT',
    DECREMENT_FOLLOWERS_COUNT: 'DECREMENT_FOLLOWERS_COUNT',
    TOGGLE_USER_ALREADY_FOLLOWING: 'TOGGLE_USER_ALREADY_FOLLOWING'
}

const mutations = {
    [mutationTypes.TOGGLE_USER_ALREADY_FOLLOWING] (state) {
        state.userAlreadyFollowing = !state.userAlreadyFollowing
    },
    [mutationTypes.INCREMENT_FOLLOWERS_COUNT] () {
        const followersElm = document.getElementById('followers')
        const updatedfollowersCount = Number(followersElm.textContent) + 1

        followersElm.innerHTML = updatedfollowersCount
    },
    [mutationTypes.DECREMENT_FOLLOWERS_COUNT] () {
        const followersElm = document.getElementById('followers')
        const updatedFollowersCount = Number(followersElm.textContent) - 1

        followersElm.innerHTML = updatedFollowersCount
    }
}

const getterTypes = {
    GET_USER_ALREADY_FOLLOWING: 'GET_USER_ALREADY_FOLLOWING'
}

const getters = {
    [getterTypes.GET_USER_ALREADY_FOLLOWING] (state) {
        return state.userAlreadyFollowing
    }
}

const actionTypes = {
    FOLLOW_PUBLISHER_PROFILE: 'FOLLOW_PUBLISHER_PROFILE',
    UNFOLLOW_PUBLISHER_PROFILE: 'UNFOLLOW_PUBLISHER_PROFILE'
}

const actions = {
    [actionTypes.FOLLOW_PUBLISHER_PROFILE] (ctx, { publisherId }) {
        const data = new FormData()

        data.append('publisher_id', publisherId)

        publisherService.follow(data, {
            successCallback: () => {
                ctx.commit(
                    mutationTypes.INCREMENT_FOLLOWERS_COUNT,
                    null,
                    { root: true }
                )
                ctx.commit(
                    mutationTypes.TOGGLE_USER_ALREADY_FOLLOWING,
                    null,
                    { root: true }
                )
            }
        })
    },
    [actionTypes.UNFOLLOW_PUBLISHER_PROFILE] (ctx, { publisherId }) {
        const data = new FormData()

        data.append('publisher_id', publisherId)

        publisherService.unFollow({ data }, {
            successCallback: () => {
                ctx.commit(
                    mutationTypes.DECREMENT_FOLLOWERS_COUNT, 
                    null,
                    { root: true }
                )
                ctx.commit(
                    mutationTypes.TOGGLE_USER_ALREADY_FOLLOWING,
                    null,
                    { root: true }
                )
            }
        })
    }
}

export const mainModuleTypes = createNamespacedTypes('main', {
    actions: actionTypes,
    getters: getterTypes,
    mutations: mutationTypes
})

const mainModule = {
    state,
    actions,
    getters,
    mutations,
    namespaced: true
}

export default mainModule