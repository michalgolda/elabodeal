function saveCartRequest (state) { state.loading = true }
function saveCartSuccess (state) {
    state.loading = false

    this.$modalManager.hide()
}
function saveCartFailure (state, errors) {
    state.loading = false
    state.errors = errors
}


function selectProductRequest (state) { state.loading = true }
function selectProductSuccess (state, { products, totalPrice }) {
    state.loading = false
    state.products = products

    const summaryTotalPriceElm = document.getElementById(
        'summary-total-price'
    )

    summaryTotalPriceElm.textContent = totalPrice
}
function selectProductFailure (state, errors) {
    state.loading = false
    state.errors = errors
}


function deselectProductRequest (state) { state.loading = true }
function deselectProductSuccess (state, { products, totalPrice }) {
    state.loading = false
    state.products = products
    
    const summaryTotalPriceElm = document.getElementById(
        'summary-total-price'
    )

    summaryTotalPriceElm.textContent = totalPrice
}
function deselectProductFailure (state, errors) {
    state.loading = false
    state.errors = errors
}


function createCheckoutSessionRequest (state) { state.loading = true }
function createCheckoutSessionSuccess (state) {
    state.loading = false

    window.location.assign('/cart/checkout/')
}
function createCheckoutSessionFailure (state, errors) {
    state.loading = false
    state.errors = errors
}


function removeProductRequest (state) { state.loading = true }
function removeProductSuccess (state, { products, totalPrice, productCount }) {
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
}
function removeProductFailure (state, errors) {
    state.loading = false
    state.errors = errors
}


export const mutationsTypes = {
    SAVE_CART_REQUEST: 'SAVE_CART_REQUEST',
    SAVE_CART_SUCCESS: 'SAVE_CART_SUCCESS',
    SAVE_CART_FAILURE: 'SAVE_CART_FAILURE',

    SELECT_PRODUCT_REQUEST: 'SELECT_PRODUCT_REQUEST',
    SELECT_PRODUCT_SUCCESS: 'SELECT_PRODUCT_SUCCESS',
    SELECT_PRODUCT_FAILURE: 'SELECT_PRODUCT_FAILURE',

    DESELECT_PRODUCT_REQUEST: 'DESELECT_PRODUCT_REQUEST',
    DESELECT_PRODUCT_SUCCESS: 'DESELECT_PRODUCT_SUCCESS',
    DESELECT_PRODUCT_FAILURE: 'DESELECT_PRODUCT_FAILURE',

    CREATE_CHECKOUT_SESSION_REQUEST: 'CREATE_CHECKOUT_SESSION_REQUEST',
    CREATE_CHECKOUT_SESSION_SUCCESS: 'CREATE_CHECKOUT_SESSION_SUCCESS',
    CREATE_CHECKOUT_SESSION_FAILURE: 'CREATE_CHECKOUT_SESSION_FAILURE',

    REMOVE_PRODUCT_REQUEST: 'REMOVE_PRODUCT_REQUEST',
    REMOVE_PRODUCT_SUCCESS: 'REMOVE_PRODUCT_SUCCESS',
    REMOVE_PRODUCT_FAILURE: 'REMOVE_PRODUCT_FAILURE'
}

const mutations = {
    [mutationsTypes.SAVE_CART_REQUEST]: saveCartRequest,
    [mutationsTypes.SAVE_CART_SUCCESS]: saveCartSuccess,
    [mutationsTypes.SAVE_CART_FAILURE]: saveCartFailure,

    [mutationsTypes.SELECT_PRODUCT_REQUEST]: selectProductRequest,
    [mutationsTypes.SELECT_PRODUCT_SUCCESS]: selectProductSuccess,
    [mutationsTypes.SELECT_PRODUCT_FAILURE]: selectProductFailure,

    [mutationsTypes.DESELECT_PRODUCT_REQUEST]: deselectProductRequest,
    [mutationsTypes.DESELECT_PRODUCT_SUCCESS]: deselectProductSuccess,
    [mutationsTypes.DESELECT_PRODUCT_FAILURE]: deselectProductFailure,

    [mutationsTypes.CREATE_CHECKOUT_SESSION_REQUEST]: createCheckoutSessionRequest,
    [mutationsTypes.CREATE_CHECKOUT_SESSION_SUCCESS]: createCheckoutSessionSuccess,
    [mutationsTypes.CREATE_CHECKOUT_SESSION_FAILURE]: createCheckoutSessionFailure,

    [mutationsTypes.REMOVE_PRODUCT_REQUEST]: removeProductRequest,
    [mutationsTypes.REMOVE_PRODUCT_SUCCESS]: removeProductSuccess,
    [mutationsTypes.REMOVE_PRODUCT_FAILURE]: removeProductFailure
}

export default mutations