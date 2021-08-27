import constants from './constants'


const mutations = {
    [constants.SAVE_CART_REQUEST] (state) { state.loading = true },
    [constants.SAVE_CART_SUCCESS] (state) { 
        state.loading = false

        this.$modalManager.hide()
    },
    [constants.SAVE_CART_FAILURE] (state, errors) { 
        state.loading = false
        state.errors = errors
    },

    [constants.SELECT_PRODUCT_REQUEST] (state) { state.loading = true },
    [constants.SELECT_PRODUCT_SUCCESS] (state, { products, totalPrice }) { 
        state.loading = false
        state.products = products

        const summaryTotalPriceElm = document.getElementById(
            'summary-total-price'
        )

        summaryTotalPriceElm.textContent = totalPrice
    },
    [constants.SELECT_PRODUCT_FAILURE] (state, errors) {
        state.loading = false
        state.errors = errors
    },

    [constants.DESELECT_PRODUCT_REQUEST] (state) { state.loading = true },
    [constants.DESELECT_PRODUCT_SUCCESS] (state, { products, totalPrice }) { 
        state.loading = false
        state.products = products
        
        const summaryTotalPriceElm = document.getElementById(
            'summary-total-price'
        )

        summaryTotalPriceElm.textContent = totalPrice
    },
    [constants.DESELECT_PRODUCT_FAILURE] (state, errors) {
        state.loading = false
        state.errors = errors
    },

    [constants.CREATE_CHECKOUT_SESSION_REQUEST] (state) { state.loading = true },
    [constants.CREATE_CHECKOUT_SESSION_SUCCESS] (state) { 
        state.loading = false

        window.location.assign('/cart/checkout/')
    },
    [constants.CREATE_CHECKOUT_SESSION_FAILURE] (state, errors) {
        state.loading = false
        state.errors = errors
    },

    [constants.REMOVE_PRODUCT_REQUEST] (state) { state.loading = true },
    [constants.REMOVE_PRODUCT_SUCCESS] (state, { products, totalPrice, productCount }) { 
        state.loading = false
        state.products = products

        const summaryTotalPriceElm = document.getElementById(
            'summary-total-price'
        )
        const navTotalPriceElm = document.getElementById('cart-total-price')
        const navProductCountElm = document.getElementById('cart-product-count')
        
        navTotalPriceElm.textContent = totalPrice
        summaryTotalPriceElm.textContent = totalPrice
        navProductCountElm.textContent = `(${ productCount })`

        document.title = `Elabodeal - Koszyk (${ productCount })`
    },
    [constants.REMOVE_PRODUCT_FAILURE] (state, errors) {
        state.loading = false
        state.errors = errors
    }
}

export default mutations