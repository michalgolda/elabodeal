import { mutationsTypes } from '@/pages/cart/store/mutations'
import actions, { actionsTypes } from '@/pages/cart/store/actions'

import { cartService, checkoutSessionService } from '@/services'


test(actionsTypes.SAVE_CART, () => {
    const ctx = { commit: jest.fn() }

    const payload = {
        title: 'test',
        description: 'test'
    }

    Object.defineProperty(cartService, 'save', {
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

    actions[actionsTypes.SAVE_CART](ctx, payload)

    expect(cartService.save).toBeCalled()

    expect(ctx.commit).toHaveBeenCalledWith(
        mutationsTypes.SAVE_CART_REQUEST
    )

    expect(ctx.commit).toHaveBeenCalledWith(
        mutationsTypes.SAVE_CART_SUCCESS
    )

    expect(ctx.commit).toHaveBeenCalledWith(
        mutationsTypes.SAVE_CART_FAILURE,
        { test: 'test' }
    )
})

test(actionsTypes.REMOVE_PRODUCT, () => {
    const ctx = { commit: jest.fn() }

    const payload = { productId: '1' }

    Object.defineProperty(cartService, 'removeProduct', {
        value: jest.fn((_, options) => {
            const { successCallback, errorCallback } = options

            successCallback({
                data: {
                    cart: {
                        products: [],
                        total_price: '0.00',
                        product_count: 0
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

    actions[actionsTypes.REMOVE_PRODUCT](ctx, payload)

    expect(cartService.removeProduct).toBeCalled()

    expect(ctx.commit).toHaveBeenCalledWith(
        mutationsTypes.REMOVE_PRODUCT_REQUEST
    )

    expect(ctx.commit).toHaveBeenCalledWith(
        mutationsTypes.REMOVE_PRODUCT_SUCCESS,
        {
            products: [],
            totalPrice: '0.00',
            productCount: 0 
        }
    )

    expect(ctx.commit).toHaveBeenCalledWith(
        mutationsTypes.REMOVE_PRODUCT_FAILURE,
        { test: 'test' }
    )
})

test(actionsTypes.SELECT_PRODUCT, () => {
    const ctx = { commit: jest.fn() }

    const payload = { productId: '1' }

    Object.defineProperty(cartService, 'selectProduct', {
        value: jest.fn((_, options) => {
            const { successCallback, errorCallback } = options

            successCallback({
                data: {
                    cart: {
                        products: [],
                        total_price_of_selected_products: '0.00'
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

    actions[actionsTypes.SELECT_PRODUCT](ctx, payload)

    expect(cartService.selectProduct).toBeCalled()

    expect(ctx.commit).toHaveBeenCalledWith(
        mutationsTypes.SELECT_PRODUCT_REQUEST
    )

    expect(ctx.commit).toHaveBeenCalledWith(
        mutationsTypes.SELECT_PRODUCT_SUCCESS,
        {
            products: [],
            totalPrice: '0.00'
        }
    )

    expect(ctx.commit).toHaveBeenCalledWith(
        mutationsTypes.SELECT_PRODUCT_FAILURE,
        { test: 'test' }
    )
})

test(actionsTypes.DESELECT_PRODUCT, () => {
    const ctx = { commit: jest.fn() }

    const payload = { productId: '1' }

    Object.defineProperty(cartService, 'deselectProduct', {
        value: jest.fn((_, options) => {
            const { successCallback, errorCallback } = options

            successCallback({
                data: {
                    cart: {
                        products: [],
                        total_price: '0.00'
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

    actions[actionsTypes.DESELECT_PRODUCT](ctx, payload)

    expect(cartService.deselectProduct).toBeCalled()

    expect(ctx.commit).toHaveBeenCalledWith(
        mutationsTypes.DESELECT_PRODUCT_REQUEST
    )

    expect(ctx.commit).toHaveBeenCalledWith(
        mutationsTypes.DESELECT_PRODUCT_SUCCESS,
        {
            products: [],
            totalPrice: '0.00'
        }
    )

    expect(ctx.commit).toHaveBeenCalledWith(
        mutationsTypes.DESELECT_PRODUCT_FAILURE,
        { test: 'test' }
    )
})

test(actionsTypes.CREATE_CHECKOUT_SESSION, () => {
    const ctx = { commit: jest.fn() }

    Object.defineProperty(checkoutSessionService, 'createSession', {
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

    actions[actionsTypes.CREATE_CHECKOUT_SESSION](ctx)

    expect(checkoutSessionService.createSession).toBeCalled()

    expect(ctx.commit).toHaveBeenCalledWith(
        mutationsTypes.CREATE_CHECKOUT_SESSION_REQUEST
    )

    expect(ctx.commit).toHaveBeenCalledWith(
        mutationsTypes.CREATE_CHECKOUT_SESSION_SUCCESS
    )

    expect(ctx.commit).toHaveBeenCalledWith(
        mutationsTypes.CREATE_CHECKOUT_SESSION_FAILURE,
        { test: 'test' }
    )
})