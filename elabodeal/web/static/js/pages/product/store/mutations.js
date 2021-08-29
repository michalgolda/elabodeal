function buyNowProductRequest (state) { state.loading = true }
function buyNowProductSuccess (state) {
    state.loading = false

    window.location.assign('/cart/')
}
function buyNowProductFailure (state, errors) {
    state.loading = false
    state.errors = errors
}


function addProductToCartRequest (state) { state.loading = true }
function addProductToCartSuccess (state, { product, cart }) {
    state.loading = false

    const navTotalPriceElm = document.getElementById('cart-total-price')
    const navProductCountElm = document.getElementById('cart-product-count')

    navTotalPriceElm.textContent = cart.total_price
    navProductCountElm.textContent = `(${ cart.product_count })`

    this.$modalManager.show('successCartUpdatedModal', {
        product: {
            author: product.author, 
            title: product.title, 
            price: product.price,
            cover_img_path: product.cover_img.path
        }
    })
}
function addProductToCartFailure (state, errors) {
    state.loading = false
    state.errors = errors
}


export const mutationsTypes = {
    BUY_NOW_PRODUCT_REQUEST: 'BUY_NOW_PRODUCT_REQUEST',
    BUY_NOW_PRODUCT_SUCCESS: 'BUY_NOW_PRODUCT_SUCCESS',
    BUY_NOW_PRODUCT_FAILURE: 'BUY_NOW_PRODUCT_FAILURE',

    ADD_PRODUCT_TO_CART_REQUEST: 'ADD_PRODUCT_TO_CART_REQUEST',
    ADD_PRODUCT_TO_CART_SUCCESS: 'ADD_PRODUCT_TO_CART_SUCCESS',
    ADD_PRODUCT_TO_CART_FAILURE: 'ADD_PRODUCT_TO_CART_FAILURE'
}

const mutations = {
    [mutationsTypes.BUY_NOW_PRODUCT_REQUEST]: buyNowProductRequest,
    [mutationsTypes.BUY_NOW_PRODUCT_SUCCESS]: buyNowProductSuccess,
    [mutationsTypes.BUY_NOW_PRODUCT_FAILURE]: buyNowProductFailure,

    [mutationsTypes.ADD_PRODUCT_TO_CART_REQUEST]: addProductToCartRequest,
    [mutationsTypes.ADD_PRODUCT_TO_CART_SUCCESS]: addProductToCartSuccess,
    [mutationsTypes.ADD_PRODUCT_TO_CART_FAILURE]: addProductToCartFailure
}

export default mutations