function followPublisherProfileRequest (state) { state.loading = true }
function followPublisherProfileSuccess (state) {
    state.loading = false
    state.userAlreadyFollowing = true

    const followersElm = document.getElementById('followers')
    const updatedfollowersCount = Number(followersElm.textContent) + 1

    followersElm.innerHTML = updatedfollowersCount
}
function followPublisherProfileFailure (state, errors) {
    state.loading = false
    state.errors = errors
}


function unfollowPublisherProfileRequest (state) { state.loading = true }
function unfollowPublisherProfileSuccess (state) {
    state.loading = false
    state.userAlreadyFollowing = false

    const followersElm = document.getElementById('followers')
    const updatedFollowersCount = Number(followersElm.textContent) - 1

    followersElm.innerHTML = updatedFollowersCount
}
function unfollowPublisherProfileFailure (state, errors) {
    state.loading = false
    state.errors = errors
}


export const mutationsTypes = {
    FOLLOW_PUBLISHER_PROFILE_REQUEST: 'FOLLOW_PUBLISHER_PROFILE_REQUEST',
    FOLLOW_PUBLISHER_PROFILE_SUCCESS: 'FOLLOW_PUBLISHER_PROFILE_SUCCESS',
    FOLLOW_PUBLISHER_PROFILE_FAILURE: 'FOLLOW_PUBLISHER_PROFILE_FAILURE',

    UNFOLLOW_PUBLISHER_PROFILE_REQUEST: 'UNFOLLOW_PUBLISHER_PROFILE_REQUEST',
    UNFOLLOW_PUBLISHER_PROFILE_SUCCESS: 'UNFOLLOW_PUBLISHER_PROFILE_SUCCESS',
    UNFOLLOW_PUBLISHER_PROFILE_FAILURE: 'UNFOLLOW_PUBLISHER_PROFILE_FAILURE' 
}

const mutations = {
    [mutationsTypes.FOLLOW_PUBLISHER_PROFILE_REQUEST]: followPublisherProfileRequest,
    [mutationsTypes.FOLLOW_PUBLISHER_PROFILE_SUCCESS]: followPublisherProfileSuccess,
    [mutationsTypes.FOLLOW_PUBLISHER_PROFILE_FAILURE]: followPublisherProfileFailure,

    [mutationsTypes.UNFOLLOW_PUBLISHER_PROFILE_REQUEST]: unfollowPublisherProfileRequest,
    [mutationsTypes.UNFOLLOW_PUBLISHER_PROFILE_SUCCESS]: unfollowPublisherProfileSuccess,
    [mutationsTypes.UNFOLLOW_PUBLISHER_PROFILE_FAILURE]: unfollowPublisherProfileFailure
}

export default mutations