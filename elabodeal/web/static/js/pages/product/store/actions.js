import { mutationsTypes } from './mutations'
import { cartService } from '@/services'


function buyNowProduct ({ commit }, { productId }) {
    const data = new FormData()

    data.append('product_id', productId)

    commit(mutationsTypes.BUY_NOW_PRODUCT_REQUEST)

    cartService.addProduct(data, {
        successCallback () {
            commit(mutationsTypes.BUY_NOW_PRODUCT_SUCCESS)
        },
        errorCallback (errorResponse) {
            const errors = errorResponse.data.error.details

            commit(
                mutationsTypes.BUY_NOW_PRODUCT_FAILURE,
                errors
            )
        }
    })
}

function addProductToCart ({ commit }, { productId }) {
    const data = new FormData()

    data.append('product_id', productId)

    commit(mutationsTypes.ADD_PRODUCT_TO_CART_REQUEST)

    cartService.addProduct(data, {
        successCallback ({ data }) {
            const { product, cart } = data;

            commit(
                mutationsTypes.ADD_PRODUCT_TO_CART_SUCCESS,
                { product, cart }
            )
        },
        errorCallback (errorResponse) {
            const errors = errorResponse.data.error.details

            commit(
                mutationsTypes.ADD_PRODUCT_TO_CART_FAILURE,
                errors
            )
        }
    })
}


export const actionsTypes = {
    BUY_NOW_PRODUCT: 'BUY_NOW_PRODUCT',
    ADD_PRODUCT_TO_CART: 'ADD_PRODUCT_TO_CART'
}

const actions = {
    [actionsTypes.BUY_NOW_PRODUCT]: buyNowProduct,
    [actionsTypes.ADD_PRODUCT_TO_CART]: addProductToCart
}

export default actions