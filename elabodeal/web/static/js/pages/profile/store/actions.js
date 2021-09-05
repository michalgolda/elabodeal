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

function updateProfile (
    { commit }, 
    { 
        bio,
        whoYouAre,
        bannerText,
        bannerProduct
    }
) {
    const data = new FormData()

    bio && data.append('bio', bio)
    whoYouAre && data.append('who_you_are', whoYouAre)
    bannerText && data.append('banner_text', bannerText)
    bannerProduct && data.append('banner_product', bannerProduct)

    commit(mutationsTypes.UPDATE_PROFILE_REQUEST)

    publisherService.updateProfile(data, {
        successCallback ({ data }) {
            const { profile } = data

            commit(mutationsTypes.UPDATE_PROFILE_SUCCESS, { profile })
        },
        errorCallback (errorResponse) {
            const errors = errorResponse.data.error.details

            commit(mutationsTypes.UPDATE_PROFILE_FAILURE, errors)
        }
    })
}

function updateProfileBannerImg ({ commit }, { bannerImg }) {
    const data = new FormData()

    bannerImg && data.append('banner_img', bannerImg)

    commit(mutationsTypes.UPDATE_PROFILE_BANNER_IMG_REQUEST)

    publisherService.updateProfileBannerImg(data, {
        successCallback ({ data }) {
            const { profile } = data

            commit(mutationsTypes.UPDATE_PROFILE_BANNER_IMG_SUCCESS, { profile })
        },
        errorCallback (errorResponse) {
            const errors = errorResponse.data.error.details

            commit(mutationsTypes.UPDATE_PROFILE_BANNER_IMG_FAILURE, errors)
        }
    })
}

function updateProfileAvatarImg ({ commit }, { avatarImg }) {
    const data = new FormData()

    avatarImg && data.append('avatar_img', avatarImg)

    commit(mutationsTypes.UPDATE_PROFILE_AVATAR_IMG_REQUEST)

    publisherService.updateProfileAvatarImg(data, {
        successCallback ({ data }) {
            const { profile } = data

            commit(mutationsTypes.UPDATE_PROFILE_AVATAR_IMG_SUCCESS, { profile })
        },
        errorCallback (errorResponse) {
            const errors = errorResponse.data.error.details

            commit(mutationsTypes.UPDATE_PROFILE_AVATAR_IMG_FAILURE, errors)
        }
    })
}


export const actionsTypes = {
    FOLLOW_PUBLISHER_PROFILE: 'FOLLOW_PUBLISHER_PROFILE',
    UNFOLLOW_PUBLISHER_PROFILE: 'UNFOLLOW_PUBLISHER_PROFILE',
    UPDATE_PROFILE: 'UPDATE_PROFILE',
    UPDATE_PROFILE_BANNER_IMG: 'UPDATE_PROFILE_BANNER_IMG',
    UPDATE_PROFILE_AVATAR_IMG: 'UPDATE_PROFILE_AVATAR_IMG'
}

const actions = {
    [actionsTypes.FOLLOW_PUBLISHER_PROFILE]: followPublisherProfile,
    [actionsTypes.UNFOLLOW_PUBLISHER_PROFILE]: unfollowPublisherProfile,
    [actionsTypes.UPDATE_PROFILE]: updateProfile,
    [actionsTypes.UPDATE_PROFILE_BANNER_IMG]: updateProfileBannerImg,
    [actionsTypes.UPDATE_PROFILE_AVATAR_IMG]: updateProfileAvatarImg
}

export default actions