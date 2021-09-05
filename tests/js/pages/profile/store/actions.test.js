import { mutationsTypes } from '@/pages/profile/store/mutations'
import actions, { actionsTypes } from '@/pages/profile/store/actions'

import { publisherService } from '@/services'


test(actionsTypes.FOLLOW_PUBLISHER_PROFILE, () => {
    const ctx = { commit: jest.fn() }

    const payload = { publisherId: '1' }

    Object.defineProperty(publisherService, 'follow', {
        value: jest.fn((_, options) => {
            const { successCallback, errorCallback } = options

            successCallback()

            errorCallback({
                data: {
                    error: {
                        details: { test: 'test' }
                    }
                }
            })
        })
    })

    actions[actionsTypes.FOLLOW_PUBLISHER_PROFILE](ctx, payload)

    expect(publisherService.follow).toBeCalled()

    expect(ctx.commit).toHaveBeenCalledWith(
        mutationsTypes.FOLLOW_PUBLISHER_PROFILE_REQUEST
    )

    expect(ctx.commit).toHaveBeenCalledWith(
        mutationsTypes.FOLLOW_PUBLISHER_PROFILE_SUCCESS
    )

    expect(ctx.commit).toHaveBeenCalledWith(
        mutationsTypes.FOLLOW_PUBLISHER_PROFILE_FAILURE,
        { test: 'test' }
    )
})

test(actionsTypes.UNFOLLOW_PUBLISHER_PROFILE, () => {
    const ctx = { commit: jest.fn() }

    const payload = { publisherId: '1' }

    Object.defineProperty(publisherService, 'unfollow', {
        value: jest.fn((_, options) => {
            const { successCallback, errorCallback } = options

            successCallback()

            errorCallback({
                data: {
                    error: {
                        details: { test: 'test' }
                    }
                }
            })
        })
    })

    actions[actionsTypes.UNFOLLOW_PUBLISHER_PROFILE](ctx, payload)

    expect(publisherService.unfollow).toBeCalled()

    expect(ctx.commit).toHaveBeenCalledWith(
        mutationsTypes.UNFOLLOW_PUBLISHER_PROFILE_REQUEST
    )

    expect(ctx.commit).toHaveBeenCalledWith(
        mutationsTypes.UNFOLLOW_PUBLISHER_PROFILE_SUCCESS
    )

    expect(ctx.commit).toHaveBeenCalledWith(
        mutationsTypes.UNFOLLOW_PUBLISHER_PROFILE_FAILURE,
        { test: 'test' }
    )
})

test(actionsTypes.UPDATE_PROFILE, () => {
    const ctx = { commit: jest.fn() }

    const payload = { 
        bio: 'test',
        whoYouAre: 'test',
        bannerText: 'test',
        bannerProduct: { id: '123' }
    }

    Object.defineProperty(publisherService, 'updateProfile', {
        value: jest.fn((_, options) => {
            const { successCallback, errorCallback } = options

            successCallback({
                data: {
                    profile: {
                        bio: 'test',
                        banner_text: 'test',
                        who_you_are: 'test',
                        banner_product: { cover_img: { path: 'test' } }
                    }
                }
            })

            errorCallback({
                data: {
                    error: {
                        details: { test: 'test' }
                    }
                }
            })
        })
    })

    actions[actionsTypes.UPDATE_PROFILE](ctx, payload)

    expect(publisherService.updateProfile).toBeCalled()

    expect(ctx.commit).toHaveBeenCalledWith(
        mutationsTypes.UPDATE_PROFILE_REQUEST
    )

    expect(ctx.commit).toHaveBeenCalledWith(
        mutationsTypes.UPDATE_PROFILE_SUCCESS,
        {
            profile: {
                bio: 'test',
                banner_text: 'test',
                who_you_are: 'test',
                banner_product: { cover_img: { path: 'test' } }
            }
        }
    )

    expect(ctx.commit).toHaveBeenCalledWith(
        mutationsTypes.UPDATE_PROFILE_FAILURE,
        { test: 'test' }
    )
})

test(actionsTypes.UPDATE_PROFILE_BANNER_IMG, () => {
    const ctx = { commit: jest.fn() }

    const payload = { bannerImg: 'test' }

    Object.defineProperty(publisherService, 'updateProfileBannerImg', {
        value: jest.fn((_, options) => {
            const { successCallback, errorCallback } = options

            successCallback({
                data: {
                    profile: { banner_img: { path: 'test' } }
                }
            })

            errorCallback({
                data: {
                    error: {
                        details: { test: 'test' }
                    }
                }
            })
        })
    })

    actions[actionsTypes.UPDATE_PROFILE_BANNER_IMG](ctx, payload)

    expect(publisherService.updateProfileBannerImg).toBeCalled()

    expect(ctx.commit).toHaveBeenCalledWith(
        mutationsTypes.UPDATE_PROFILE_BANNER_IMG_REQUEST
    )

    expect(ctx.commit).toHaveBeenCalledWith(
        mutationsTypes.UPDATE_PROFILE_BANNER_IMG_SUCCESS,
        { profile: { banner_img: { path: 'test' } } }
    )

    expect(ctx.commit).toHaveBeenCalledWith(
        mutationsTypes.UPDATE_PROFILE_BANNER_IMG_FAILURE,
        { test: 'test' }
    )
})

test(actionsTypes.UPDATE_PROFILE_AVATAR_IMG, () => {
    const ctx = { commit: jest.fn() }

    const payload = { avatarImg: 'test' }

    Object.defineProperty(publisherService, 'updateProfileAvatarImg', {
        value: jest.fn((_, options) => {
            const { successCallback, errorCallback } = options

            successCallback({
                data: {
                    profile: { avatar_img: { path: 'test' } }
                }
            })

            errorCallback({
                data: {
                    error: {
                        details: { test: 'test' }
                    }
                }
            })
        })
    })

    actions[actionsTypes.UPDATE_PROFILE_AVATAR_IMG](ctx, payload)

    expect(publisherService.updateProfileAvatarImg).toBeCalled()

    expect(ctx.commit).toHaveBeenCalledWith(
        mutationsTypes.UPDATE_PROFILE_AVATAR_IMG_REQUEST
    )

    expect(ctx.commit).toHaveBeenCalledWith(
        mutationsTypes.UPDATE_PROFILE_AVATAR_IMG_SUCCESS,
        { profile: { avatar_img: { path: 'test' } } }
    )

    expect(ctx.commit).toHaveBeenCalledWith(
        mutationsTypes.UPDATE_PROFILE_AVATAR_IMG_FAILURE,
        { test: 'test' }
    )
})