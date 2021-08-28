import { mutationsTypes } from './mutations'
import { publisherService } from '@/services'


function followPublisherProfile ({ commit }, { publisherId }) {
    const data = new FormData()

    data.append('publisher_id', publisherId)

    commit(mutationsTypes.FOLLOW_PUBLISHER_PROFILE_REQUEST)

    publisherService.follow(data, {
        successCallback () {
            commit(mutationsTypes.FOLLOW_PUBLISHER_PROFILE_SUCCESS)
        },
        errorCallback (errorResponse) {
            const errors = errorResponse.data.error.details

            commit(
                mutationsTypes.FOLLOW_PUBLISHER_PROFILE_FAILURE,
                errors
            )
        }
    })
}

function unfollowPublisherProfile ({ commit }, { publisherId }) {
    const data = new FormData()

    data.append('publisher_id', publisherId)

    commit(mutationsTypes.UNFOLLOW_PUBLISHER_PROFILE_REQUEST)

    publisherService.unfollow({ data }, {
        successCallback () {
            commit(mutationsTypes.UNFOLLOW_PUBLISHER_PROFILE_SUCCESS)
        },
        errorCallback (errorResponse) {
            const errors = errorResponse.data.error.details

            commit(
                mutationsTypes.UNFOLLOW_PUBLISHER_PROFILE_FAILURE,
                errors
            )
        }
    })
}


export const actionsTypes = {
    FOLLOW_PUBLISHER_PROFILE: 'FOLLOW_PUBLISHER_PROFILE',
    UNFOLLOW_PUBLISHER_PROFILE: 'UNFOLLOW_PUBLISHER_PROFILE'
}

const actions = {
    [actionsTypes.FOLLOW_PUBLISHER_PROFILE]: followPublisherProfile,
    [actionsTypes.UNFOLLOW_PUBLISHER_PROFILE]: unfollowPublisherProfile
}

export default actions