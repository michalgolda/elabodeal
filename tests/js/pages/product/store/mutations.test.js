import mutations, { mutationsTypes } from '@/pages/product/store/mutations'


describe('BUY_NOW_PRODUCT', () => {
    test(mutationsTypes.BUY_NOW_PRODUCT_REQUEST, () => {
        const state = { loading: false }

        mutations[mutationsTypes.BUY_NOW_PRODUCT_REQUEST](state)

        expect(state).toStrictEqual({ loading: true })
    })

    test(mutationsTypes.BUY_NOW_PRODUCT_SUCCESS, () => {
        const state = { loading: true }

        delete window.location

        window.location = { assign: jest.fn() }

        mutations[mutationsTypes.BUY_NOW_PRODUCT_SUCCESS](state)

        expect(state).toStrictEqual({ loading: false })

        expect(window.location.assign).toHaveBeenCalledWith('/cart/')
    })

    test(mutationsTypes.BUY_NOW_PRODUCT_FAILURE, () => {
        const state = { loading: true, errors: {} }

        mutations[mutationsTypes.BUY_NOW_PRODUCT_FAILURE](state, {
            test: 'test'
        })

        expect(state).toStrictEqual({ 
            loading: false, 
            errors: { test: 'test' }
        })
    })
})

describe('ADD_PRODUCT_TO_CART', () => {
    test(mutationsTypes.ADD_PRODUCT_TO_CART_REQUEST, () => {
        const state = { loading: false }

        mutations[mutationsTypes.ADD_PRODUCT_TO_CART_REQUEST](state)

        expect(state).toStrictEqual({ loading: true })
    })

    test(mutationsTypes.ADD_PRODUCT_TO_CART_SUCCESS, () => {
        const state = { loading: true }

        document.body.innerHTML = `
            <span id="cart-total-price">0.00</span>
            <span id="cart-product-count">0</span>
        `

        mutations['$modalManager'] = { show: jest.fn() }

        mutations[mutationsTypes.ADD_PRODUCT_TO_CART_SUCCESS](state, {
            product: {
                author: 'test',
                title: 'test',
                price: '2.00',
                cover_img: { path: 'test' }
            },
            cart: {
                total_price: '2.00',
                product_count: 1
            }
        })

        expect(state).toStrictEqual({ loading: false })

        const navTotalPriceElm = document.getElementById('cart-total-price')
        const navProductCountElm = document.getElementById('cart-product-count')

        expect(navTotalPriceElm.textContent).toBe('2.00')
        expect(navProductCountElm.textContent).toBe('(1)')

        expect(mutations.$modalManager.show).toHaveBeenCalledWith(
            'successCartUpdatedModal',
            {
                product: {
                    author: 'test',
                    title: 'test',
                    price: '2.00',
                    cover_img_path: 'test'
                }
            }
        )
    })

    test(mutationsTypes.ADD_PRODUCT_TO_CART_FAILURE, () => {
        const state = { loading: true, errors: {} }

        mutations[mutationsTypes.ADD_PRODUCT_TO_CART_FAILURE](state, {
            test: 'test'
        })

        expect(state).toStrictEqual({ 
            loading: false,
            errors: { test: 'test' } 
        })
    })
})