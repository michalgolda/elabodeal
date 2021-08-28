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