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


function updateProfileRequest (state) { 
    state.loading = true 
    state.errors = {}
}
function updateProfileSuccess (state, { profile }) {
    state.loading = false
    state.profile = profile

    const bioElm = document.querySelector('#bio')
    const whoYouAreElm = document.querySelector('#who-you-are')
    const bannerTextElm = document.querySelector('#banner-text')

    bioElm.textContent = profile.bio
    bannerTextElm.textContent = profile.banner_text
    whoYouAreElm.textContent = profile.who_you_are

    const bannerProduct = profile.banner_product

    const bannerProductElm = document.querySelector('#banner-product')

    if (!bannerProduct) {
        bannerProductElm && bannerProductElm.remove()

        return
    }

    if (!bannerProductElm) {
        const newBannerProductElm = document.createElement('img')

        newBannerProductElm.id = 'banner-product'
        newBannerProductElm.classList.add('profileBanner__productHighlight')
        newBannerProductElm.src = profile.banner_product.cover_img.path

        const profileBannerContentElm = document.querySelector('.profileBanner__content')

        profileBannerContentElm.appendChild(newBannerProductElm)
    } else {
        bannerProductElm.src = profile.banner_product.cover_img.path
    }

    this.$modalManager.hide()
}
function updateProfileFailure (state, errors) {
    state.loading = false
    state.errors = errors
}


function updateProfileBannerImgRequest (state) {
    state.loading = true
    state.errors = {}
}
function updateProfileBannerImgSuccess (state, { profile }) {
    state.loading = false
    state.profile = profile

    const bannerImg = profile.banner_img
    const bannerImgElm = document.querySelector('.profileBanner__img')

    if (bannerImg) {
        if (bannerImgElm.tagName === 'img') {
            bannerImgElm.src = bannerImg.path
        } else {
            const newBannerImgElm = document.createElement('img')

            newBannerImgElm.src = bannerImg.path
            newBannerImgElm.classList.add('profileBanner__img')
        
            bannerImgElm.replaceWith(newBannerImgElm)
        }
    } else {
        const newBannerImgElm = document.createElement('div')

        newBannerImgElm.classList.add('profileBanner__img')

        bannerImgElm.replaceWith(newBannerImgElm)
    }
}
function updateProfileBannerImgFailure (state, errors) {
    state.loading = false
    state.errors = errors
}


function updateProfileAvatarImgRequest (state) {
    state.loading = true
    state.errors = {}
}
function updateProfileAvatarImgSuccess (state, { profile }) {
    state.loading = false
    state.profile = profile

    const avatarImg = profile.avatar_img
    const avatarImgElm = document.querySelector('.profileBadge__avatar')

    if (avatarImg) {
        if (avatarImgElm.tagName === 'img') {
            avatarImgElm.src = avatarImg.path
        } else {
            const newAvatarImgElm = document.createElement('img')

            newAvatarImgElm.src = avatarImg.path
            newAvatarImgElm.classList.add('profileBadge__avatar')
        
            avatarImgElm.replaceWith(newAvatarImgElm)
        }
    } else {
        const newAvatarImgElm = document.createElement('div')

        newAvatarImgElm.classList.add('profileBadge__avatar')

        avatarImgElm.replaceWith(newAvatarImgElm)
    }
}
function updateProfileAvatarImgFailure (state, errors) {
    state.loading = false
    state.errors = errors
}

export const mutationsTypes = {
    FOLLOW_PUBLISHER_PROFILE_REQUEST: 'FOLLOW_PUBLISHER_PROFILE_REQUEST',
    FOLLOW_PUBLISHER_PROFILE_SUCCESS: 'FOLLOW_PUBLISHER_PROFILE_SUCCESS',
    FOLLOW_PUBLISHER_PROFILE_FAILURE: 'FOLLOW_PUBLISHER_PROFILE_FAILURE',

    UNFOLLOW_PUBLISHER_PROFILE_REQUEST: 'UNFOLLOW_PUBLISHER_PROFILE_REQUEST',
    UNFOLLOW_PUBLISHER_PROFILE_SUCCESS: 'UNFOLLOW_PUBLISHER_PROFILE_SUCCESS',
    UNFOLLOW_PUBLISHER_PROFILE_FAILURE: 'UNFOLLOW_PUBLISHER_PROFILE_FAILURE',

    UPDATE_PROFILE_REQUEST: 'UPDATE_PROFILE_REQUEST',
    UPDATE_PROFILE_SUCCESS: 'UPDATE_PROFILE_SUCCESS',
    UPDATE_PROFILE_FAILURE: 'UPDATE_PROFILE_FAILURE',

    UPDATE_PROFILE_BANNER_IMG_REQUEST: 'UPDATE_PROFILE_BANNER_IMG_REQUEST',
    UPDATE_PROFILE_BANNER_IMG_SUCCESS: 'UPDATE_PROFILE_BANNER_IMG_SUCCESS',
    UPDATE_PROFILE_BANNER_IMG_FAILURE: 'UPDATE_PROFILE_BANNER_IMG_FAILURE',

    UPDATE_PROFILE_AVATAR_IMG_REQUEST: 'UPDATE_PROFILE_AVATAR_IMG_REQUEST',
    UPDATE_PROFILE_AVATAR_IMG_SUCCESS: 'UPDATE_PROFILE_AVATAR_IMG_SUCCESS',
    UPDATE_PROFILE_AVATAR_IMG_FAILURE: 'UPDATE_PROFILE_AVATAR_IMG_FAILURE'
}

const mutations = {
    [mutationsTypes.FOLLOW_PUBLISHER_PROFILE_REQUEST]: followPublisherProfileRequest,
    [mutationsTypes.FOLLOW_PUBLISHER_PROFILE_SUCCESS]: followPublisherProfileSuccess,
    [mutationsTypes.FOLLOW_PUBLISHER_PROFILE_FAILURE]: followPublisherProfileFailure,

    [mutationsTypes.UNFOLLOW_PUBLISHER_PROFILE_REQUEST]: unfollowPublisherProfileRequest,
    [mutationsTypes.UNFOLLOW_PUBLISHER_PROFILE_SUCCESS]: unfollowPublisherProfileSuccess,
    [mutationsTypes.UNFOLLOW_PUBLISHER_PROFILE_FAILURE]: unfollowPublisherProfileFailure,

    [mutationsTypes.UPDATE_PROFILE_REQUEST]: updateProfileRequest,
    [mutationsTypes.UPDATE_PROFILE_SUCCESS]: updateProfileSuccess,
    [mutationsTypes.UPDATE_PROFILE_FAILURE]: updateProfileFailure,

    [mutationsTypes.UPDATE_PROFILE_BANNER_IMG_REQUEST]: updateProfileBannerImgRequest,
    [mutationsTypes.UPDATE_PROFILE_BANNER_IMG_SUCCESS]: updateProfileBannerImgSuccess,
    [mutationsTypes.UPDATE_PROFILE_BANNER_IMG_FAILURE]: updateProfileBannerImgFailure,

    [mutationsTypes.UPDATE_PROFILE_AVATAR_IMG_REQUEST]: updateProfileAvatarImgRequest,
    [mutationsTypes.UPDATE_PROFILE_AVATAR_IMG_SUCCESS]: updateProfileAvatarImgSuccess,
    [mutationsTypes.UPDATE_PROFILE_AVATAR_IMG_FAILURE]: updateProfileAvatarImgFailure
}

export default mutations