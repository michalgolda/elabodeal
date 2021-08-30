import { checkoutSessionService } from '@/services'
import { mutationsTypes } from '@/pages/cartCheckout/store/mutations'
import actions, { actionsTypes } from '@/pages/cartCheckout/store/actions'


test(actionsTypes.SUCCEED_CHECKOUT_SESSION, () => {
    const ctx = { commit: jest.fn() }

    const payload = { firstName: 'test' }

    Object.defineProperty(checkoutSessionService, 'succeedSession', {
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

    actions[actionsTypes.SUCCEED_CHECKOUT_SESSION](ctx, payload)

    expect(ctx.commit).toHaveBeenCalledWith(
        mutationsTypes.SUCCEED_CHECKOUT_SESSION_REQUEST
    )

    expect(checkoutSessionService.succeedSession).toBeCalled()

    expect(ctx.commit).toHaveBeenCalledWith(
        mutationsTypes.SUCCEED_CHECKOUT_SESSION_SUCCESS,
        { firstName: 'test' }
    )

    expect(ctx.commit).toHaveBeenCalledWith(
        mutationsTypes.SUCCEED_CHECKOUT_SESSION_FAILURE,
        { test: 'test' }
    )
})

test(actionsTypes.CANCEL_CHECKOUT_SESSION, () => {
    const ctx = { commit: jest.fn() }

    Object.defineProperty(checkoutSessionService, 'removeSession', {
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

    actions[actionsTypes.CANCEL_CHECKOUT_SESSION](ctx)

    expect(ctx.commit).toHaveBeenCalledWith(
        mutationsTypes.CANCEL_CHECKOUT_SESSION_REQUEST
    )

    expect(checkoutSessionService.removeSession).toBeCalled()

    expect(ctx.commit).toHaveBeenCalledWith(
        mutationsTypes.CANCEL_CHECKOUT_SESSION_SUCCESS
    )

    expect(ctx.commit).toHaveBeenCalledWith(
        mutationsTypes.CANCEL_CHECKOUT_SESSION_FAILURE,
        { test: 'test' }
    )
})

test(actionsTypes.UPDATE_CHECKOUT_SESSION, () => {
    const ctx = { commit: jest.fn() }

    const payload = {
        email: 'test',
        lastName: 'test',
        firstName: 'test'
    }

    Object.defineProperty(checkoutSessionService, 'updateSession', {
        value: jest.fn((_, options) => {
            const { successCallback, errorCallback } = options

            successCallback({ data: { delivery: payload } })

            errorCallback({
                data: {
                    error: {
                        details: { test: 'test' }
                    }
                }
            })
        })
    })

    actions[actionsTypes.UPDATE_CHECKOUT_SESSION](ctx, payload)

    expect(ctx.commit).toHaveBeenCalledWith(
        mutationsTypes.UPDATE_CHECKOUT_SESSION_REQUEST
    )

    expect(checkoutSessionService.updateSession).toBeCalled()

    expect(ctx.commit).toHaveBeenCalledWith(
        mutationsTypes.UPDATE_CHECKOUT_SESSION_SUCCESS,
        {
            email: 'test',
            firstName: 'test',
            lastName: 'test'
        }
    )

    expect(ctx.commit).toHaveBeenCalledWith(
        mutationsTypes.UPDATE_CHECKOUT_SESSION_FAILURE,
        { test: 'test' }
    )
})