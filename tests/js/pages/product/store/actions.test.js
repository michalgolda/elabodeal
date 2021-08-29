import { cartService } from '@/services'
import { mutationsTypes } from '@/pages/product/store/mutations'
import actions, { actionsTypes } from '@/pages/product/store/actions'


test(actionsTypes.BUY_NOW_PRODUCT, () => {
    const ctx = { commit: jest.fn() }

    const payload = { productId: '1' }

    Object.defineProperty(cartService, 'addProduct', {
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

    actions[actionsTypes.BUY_NOW_PRODUCT](ctx, payload)

    expect(ctx.commit).toHaveBeenCalledWith(
        mutationsTypes.BUY_NOW_PRODUCT_REQUEST
    )

    expect(cartService.addProduct).toBeCalled()

    expect(ctx.commit).toHaveBeenCalledWith(
        mutationsTypes.BUY_NOW_PRODUCT_SUCCESS
    )

    expect(ctx.commit).toHaveBeenCalledWith(
        mutationsTypes.BUY_NOW_PRODUCT_FAILURE,
        { test: 'test' }
    )
})

test(actionsTypes.ADD_PRODUCT_TO_CART, () => {
    const ctx = { commit: jest.fn() }

    const payload = { productId: '1' }

    Object.defineProperty(cartService, 'addProduct', {
        value: jest.fn((_, options) => {
            const { successCallback, errorCallback } = options

            successCallback({
                data: {
                    product: { id: '1' },
                    cart: { total_price: '2.00' }
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

    actions[actionsTypes.ADD_PRODUCT_TO_CART](ctx, payload)

    expect(ctx.commit).toHaveBeenCalledWith(
        mutationsTypes.ADD_PRODUCT_TO_CART_REQUEST
    )

    expect(cartService.addProduct).toBeCalled()

    expect(ctx.commit).toHaveBeenCalledWith(
        mutationsTypes.ADD_PRODUCT_TO_CART_SUCCESS,
        {
            product: { id: '1' },
            cart: { total_price: '2.00' }
        }
    )

    expect(ctx.commit).toHaveBeenCalledWith(
        mutationsTypes.ADD_PRODUCT_TO_CART_FAILURE,
        { test: 'test' }
    )
})