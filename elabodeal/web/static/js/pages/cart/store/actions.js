import constants from './constants'
import { cartService, checkoutSessionService } from '@/services'


function saveCart ({ commit }, { title, description }) {
    const data = new FormData()
    
    data.append('title', title)
    data.append('description', description)
    
    commit(constants.SAVE_CART_REQUEST)
    
    cartService.save(data, {
        successCallback () { 
            commit(constants.SAVE_CART_SUCCESS) 
        },
        errorCallback (errorResponse) {
            const errors = errorResponse.data.error.details

            commit(
                constants.SAVE_CART_FAILURE,
                errors
            )
        }
    })
}

function removeProduct ({ commit }, { productId }) {
    const data = new FormData()

    data.append('product_id', productId)

    commit(constants.REMOVE_PRODUCT_REQUEST)

    cartService.removeProduct({ data }, {
        successCallback ({ data }) {
            const { cart } = data

            commit(
                constants.REMOVE_PRODUCT_SUCCESS,
                {
                    products: cart.products,
                    totalPrice: cart.total_price,
                    productCount: cart.product_count
                }
            )
        },
        errorCallback (errorResponse) {
            const errors = errorResponse.data.error.details

            commit(
                constants.REMOVE_PRODUCT_FAILURE,
                errors
            )
        }
    })
}

function selectProduct ({ commit }, { productId }) {
    const data = new FormData()

    data.append('product_id', productId)

    commit(constants.SELECT_PRODUCT_REQUEST)

    cartService.selectProduct(data, {
        successCallback ({ data }) {
            const { cart } = data

            commit(
                constants.SELECT_PRODUCT_SUCCESS,
                {
                    products: cart.products,
                    totalPrice: cart.total_price_of_selected_products
                }
            )
        },
        errorCallback (errorResponse) {
            const errors = errorResponse.data.error.details

            commit(
                constants.SELECT_PRODUCT_FAILURE,
                errors
            )
        }
    })
}

function deselectProduct ({ commit }, { productId }) {
    const data = new FormData()

    data.append('product_id', productId)

    commit(constants.DESELECT_PRODUCT_REQUEST)

    cartService.deselectProduct(data, {
        successCallback ({ data }) {
            const { cart } = data

            commit(
                constants.DESELECT_PRODUCT_SUCCESS,
                {
                    products: cart.products,
                    totalPrice: cart.total_price
                }    
            )
        },
        errorCallback (errorResponse) {
            const errors = errorResponse.data.error.details

            commit(
                constants.DESELECT_PRODUCT_FAILURE,
                errors
            )
        }
    })
}

function createCheckoutSession ({ commit }) {
    commit(constants.CREATE_CHECKOUT_SESSION_REQUEST)
    
    checkoutSessionService.createSession(null, {
        successCallback () {
            commit(constants.CREATE_CHECKOUT_SESSION_SUCCESS)
        },
        errorCallback (errorResponse) {
            const errors = errorResponse.data.error.details
            
            commit(
                constants.CREATE_CHECKOUT_SESSION_FAILURE,
                errors
            )
        }
    })
}

const actions = {
    saveCart,
    removeProduct,
    selectProduct,
    deselectProduct,
    createCheckoutSession
}

export default actions