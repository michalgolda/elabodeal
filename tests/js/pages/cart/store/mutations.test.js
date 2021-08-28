import mutations, { mutationsTypes } from '../../../../../elabodeal/web/static/js/pages/cart/store/mutations'


describe('SAVE_CART', () => {
    test(mutationsTypes.SAVE_CART_REQUEST, () => {
        const state = { loading: false }
    
        mutations[mutationsTypes.SAVE_CART_REQUEST](state)
    
        expect(state).toStrictEqual({ loading: true })
    })
    
    test(mutationsTypes.SAVE_CART_SUCCESS, () => {
        const state = { loading: true }
    
        mutations['$modalManager'] = { hide: jest.fn() }
    
        mutations[mutationsTypes.SAVE_CART_SUCCESS](state)
    
        expect(state).toStrictEqual({ loading: false })
        expect(mutations.$modalManager.hide).toHaveBeenCalled()
    })
    
    test(mutationsTypes.SAVE_CART_FAILURE, () => {
        const state = { loading: true, errors: {} }
    
        mutations[mutationsTypes.SAVE_CART_FAILURE](
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
    test(mutationsTypes.SELECT_PRODUCT_REQUEST, () => {
        const state = { loading: false }

        mutations[mutationsTypes.SELECT_PRODUCT_REQUEST](state)

        expect(state).toStrictEqual({ loading: true })
    })

    test(mutationsTypes.SELECT_PRODUCT_SUCCESS, () => {
        const state = { loading: true, products: [] }

        document.body.innerHTML = `
            <span id="summary-total-price">0.00</span>
        `

        mutations[mutationsTypes.SELECT_PRODUCT_SUCCESS](state, {
            products: [{ id: 1 }],
            totalPrice: '2.00'
        })

        const summaryTotalPriceElm = document.getElementById(
            'summary-total-price'
        )

        expect(summaryTotalPriceElm.textContent).toBe('2.00')
    })

    test(mutationsTypes.SELECT_PRODUCT_FAILURE, () => {
        const state = { loading: true, errors: {} }

        mutations[mutationsTypes.SELECT_PRODUCT_FAILURE](state, {
            test: 'test'
        })

        expect(state).toStrictEqual({
            loading: false,
            errors: { test: 'test' }
        })
    })
})

describe('DESELECT_PRODUCT', () => {
    test(mutationsTypes.DESELECT_PRODUCT_REQUEST, () => {
        const state = { loading: false }

        mutations[mutationsTypes.DESELECT_PRODUCT_REQUEST](state)

        expect(state).toStrictEqual({ loading: true })
    })

    test(mutationsTypes.DESELECT_PRODUCT_SUCCESS, () => {
        const state = { loading: true, products: [{ id: 1 }] }

        document.body.innerHTML = `
            <span id="summary-total-price">2.00</span>
        `

        mutations[mutationsTypes.DESELECT_PRODUCT_SUCCESS](state, {
            products: [],
            totalPrice: '0.00'
        })

        const summaryTotalPriceElm = document.getElementById(
            'summary-total-price'
        )

        expect(summaryTotalPriceElm.textContent).toBe('0.00')
    })

    test(mutationsTypes.DESELECT_PRODUCT_FAILURE, () => {
        const state = { loading: true, errors: {} }

        mutations[mutationsTypes.DESELECT_PRODUCT_FAILURE](state, {
            test: 'test'
        })

        expect(state).toStrictEqual({
            loading: false,
            errors: { test: 'test' }
        })
    })
})

describe('CREATE_CHECKOUT_SESSION', () => {
    test(mutationsTypes.CREATE_CHECKOUT_SESSION_REQUEST, () => {
        const state = { loading: false }

        mutations[mutationsTypes.CREATE_CHECKOUT_SESSION_REQUEST](state)

        expect(state).toStrictEqual({ loading: true })
    })

    test(mutationsTypes.CREATE_CHECKOUT_SESSION_SUCCESS, () => {
        const state = { loading: true }
        
        delete window.location

        window.location = { assign: jest.fn() }

        mutations[mutationsTypes.CREATE_CHECKOUT_SESSION_SUCCESS](state)

        expect(window.location.assign).toHaveBeenCalledWith('/cart/checkout/')
    })

    test(mutationsTypes.CREATE_CHECKOUT_SESSION_FAILURE, () => {
        const state = { loading: true, errors: {} }

        mutations[mutationsTypes.CREATE_CHECKOUT_SESSION_FAILURE](state, {
            test: 'test'
        })

        expect(state).toStrictEqual({
            loading: false,
            errors: { test: 'test' }
        })
    })
})

describe('REMOVE_PRODUCT', () => {
    test(mutationsTypes.REMOVE_PRODUCT_REQUEST, () => {
        const state = { loading: false }

        mutations[mutationsTypes.REMOVE_PRODUCT_REQUEST](state)

        expect(state).toStrictEqual({ loading: true })
    })

    test(mutationsTypes.REMOVE_PRODUCT_SUCCESS, () => {
        const state = { loading: true, products: [{ id: 1 }] }

        document.title = ''

        document.body.innerHTML = `
            <span id="summary-total-price">2.00</span>
            <span id="cart-total-price">2.00</span>
            <span id="cart-product-count">1</span>
        `

        mutations[mutationsTypes.REMOVE_PRODUCT_SUCCESS](state, {
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

    test(mutationsTypes.DESELECT_PRODUCT_FAILURE, () => {
        const state = { loading: true, errors: {} }

        mutations[mutationsTypes.DESELECT_PRODUCT_FAILURE](state, {
            test: 'test'
        })

        expect(state).toStrictEqual({
            loading: false,
            errors: { test: 'test' }
        })
    })
})