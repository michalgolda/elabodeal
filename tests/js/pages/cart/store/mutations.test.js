import mutations from '../../../../../elabodeal/web/static/js/pages/cart/store/mutations'
import constants from '../../../../../elabodeal/web/static/js/pages/cart/store/constants'


describe('SAVE_CART', () => {
    test(constants.SAVE_CART_REQUEST, () => {
        const state = { loading: false }
    
        mutations[constants.SAVE_CART_REQUEST](state)
    
        expect(state).toStrictEqual({ loading: true })
    })
    
    test(constants.SAVE_CART_SUCCESS, () => {
        const state = { loading: true }
    
        mutations['$modalManager'] = { hide: jest.fn() }
    
        mutations[constants.SAVE_CART_SUCCESS](state)
    
        expect(state).toStrictEqual({ loading: false })
        expect(mutations.$modalManager.hide).toHaveBeenCalled()
    })
    
    test(constants.SAVE_CART_FAILURE, () => {
        const state = { loading: true, errors: {} }
    
        mutations[constants.SAVE_CART_FAILURE](
            state, 
            { test: 'test' }
        )
    
        expect(state).toStrictEqual({ 
            loading: false, 
            errors: { test: 'test' } 
        })
    })
})

describe('SELECT_PRODUCT', () => {
    test(constants.SELECT_PRODUCT_REQUEST, () => {
        const state = { loading: false }

        mutations[constants.SELECT_PRODUCT_REQUEST](state)

        expect(state).toStrictEqual({ loading: true })
    })

    test(constants.SELECT_PRODUCT_SUCCESS, () => {
        const state = { loading: true, products: [] }

        document.body.innerHTML = `
            <span id="summary-total-price">0.00</span>
        `

        mutations[constants.SELECT_PRODUCT_SUCCESS](state, {
            products: [{ id: 1 }],
            totalPrice: '2.00'
        })

        const summaryTotalPriceElm = document.getElementById(
            'summary-total-price'
        )

        expect(summaryTotalPriceElm.textContent).toBe('2.00')
    })

    test(constants.SELECT_PRODUCT_FAILURE, () => {
        const state = { loading: true, errors: {} }

        mutations[constants.SELECT_PRODUCT_FAILURE](state, {
            test: 'test'
        })

        expect(state).toStrictEqual({
            loading: false,
            errors: { test: 'test' }
        })
    })
})

describe('DESELECT_PRODUCT', () => {
    test(constants.DESELECT_PRODUCT_REQUEST, () => {
        const state = { loading: false }

        mutations[constants.DESELECT_PRODUCT_REQUEST](state)

        expect(state).toStrictEqual({ loading: true })
    })

    test(constants.DESELECT_PRODUCT_SUCCESS, () => {
        const state = { loading: true, products: [{ id: 1 }] }

        document.body.innerHTML = `
            <span id="summary-total-price">2.00</span>
        `

        mutations[constants.DESELECT_PRODUCT_SUCCESS](state, {
            products: [],
            totalPrice: '0.00'
        })

        const summaryTotalPriceElm = document.getElementById(
            'summary-total-price'
        )

        expect(summaryTotalPriceElm.textContent).toBe('0.00')
    })

    test(constants.DESELECT_PRODUCT_FAILURE, () => {
        const state = { loading: true, errors: {} }

        mutations[constants.DESELECT_PRODUCT_FAILURE](state, {
            test: 'test'
        })

        expect(state).toStrictEqual({
            loading: false,
            errors: { test: 'test' }
        })
    })
})

describe('CREATE_CHECKOUT_SESSION', () => {
    test(constants.CREATE_CHECKOUT_SESSION_REQUEST, () => {
        const state = { loading: false }

        mutations[constants.CREATE_CHECKOUT_SESSION_REQUEST](state)

        expect(state).toStrictEqual({ loading: true })
    })

    test(constants.CREATE_CHECKOUT_SESSION_SUCCESS, () => {
        const state = { loading: true }
        
        delete window.location

        window.location = { assign: jest.fn() }

        mutations[constants.CREATE_CHECKOUT_SESSION_SUCCESS](state)

        expect(window.location.assign).toHaveBeenCalledWith('/cart/checkout/')
    })

    test(constants.CREATE_CHECKOUT_SESSION_FAILURE, () => {
        const state = { loading: true, errors: {} }

        mutations[constants.CREATE_CHECKOUT_SESSION_FAILURE](state, {
            test: 'test'
        })

        expect(state).toStrictEqual({
            loading: false,
            errors: { test: 'test' }
        })
    })
})

describe('REMOVE_PRODUCT', () => {
    test(constants.REMOVE_PRODUCT_REQUEST, () => {
        const state = { loading: false }

        mutations[constants.REMOVE_PRODUCT_REQUEST](state)

        expect(state).toStrictEqual({ loading: true })
    })

    test(constants.REMOVE_PRODUCT_SUCCESS, () => {
        const state = { loading: true, products: [{ id: 1 }] }

        document.title = ''

        document.body.innerHTML = `
            <span id="summary-total-price">2.00</span>
            <span id="cart-total-price">2.00</span>
            <span id="cart-product-count">1</span>
        `

        mutations[constants.REMOVE_PRODUCT_SUCCESS](state, {
            products: [],
            totalPrice: '0.00',
            productCount: 0
        })

        const summaryTotalPriceElm = document.getElementById(
            'summary-total-price'
        )

        const navTotalPriceElm = document.getElementById(
            'cart-total-price'
        )

        const navProductCountElm = document.getElementById(
            'cart-product-count'
        )

        expect(state).toStrictEqual({
            loading: false,
            products: []
        })

        expect(navTotalPriceElm.textContent).toBe('0.00')
        expect(navProductCountElm.textContent).toBe('(0)')
        expect(summaryTotalPriceElm.textContent).toBe('0.00')
        
        expect(document.title).toBe('Elabodeal - Koszyk (0)')
    })

    test(constants.DESELECT_PRODUCT_FAILURE, () => {
        const state = { loading: true, errors: {} }

        mutations[constants.DESELECT_PRODUCT_FAILURE](state, {
            test: 'test'
        })

        expect(state).toStrictEqual({
            loading: false,
            errors: { test: 'test' }
        })
    })
})