import { mutationsTypes } from './types'
import { cartService, checkoutSessionService } from '@/services'


function saveCart ({ commit }, { title, description }) {
    const data = new FormData()
    
    data.append('title', title)
    data.append('description', description)
    
    commit(mutationsTypes.SAVE_CART_REQUEST)
    
    cartService.save(data, {
        successCallback () { 
            commit(mutationsTypes.SAVE_CART_SUCCESS) 
        },
        errorCallback (errorResponse) {
            const errors = errorResponse.data.error.details

            commit(
                mutationsTypes.SAVE_CART_FAILURE,
                errors
            )
        }
    })
}

function removeProduct ({ commit }, { productId }) {
    const data = new FormData()

    data.append('product_id', productId)

    commit(mutationsTypes.REMOVE_PRODUCT_REQUEST)

    cartService.removeProduct({ data }, {
        successCallback ({ data }) {
            const { cart } = data

            commit(
                mutationsTypes.REMOVE_PRODUCT_SUCCESS,
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
                mutationsTypes.REMOVE_PRODUCT_FAILURE,
                errors
            )
        }
    })
}

function selectProduct ({ commit }, { productId }) {
    const data = new FormData()

    data.append('product_id', productId)

    commit(mutationsTypes.SELECT_PRODUCT_REQUEST)

    cartService.selectProduct(data, {
        successCallback ({ data }) {
            const { cart } = data

            commit(
                mutationsTypes.SELECT_PRODUCT_SUCCESS,
                {
                    products: cart.products,
                    totalPrice: cart.total_price_of_selected_products
                }
            )
        },
        errorCallback (errorResponse) {
            const errors = errorResponse.data.error.details

            commit(
                mutationsTypes.SELECT_PRODUCT_FAILURE,
                errors
            )
        }
    })
}

function deselectProduct ({ commit }, { productId }) {
    const data = new FormData()

    data.append('product_id', productId)

    commit(mutationsTypes.DESELECT_PRODUCT_REQUEST)

    cartService.deselectProduct(data, {
        successCallback ({ data }) {
            const { cart } = data

            commit(
                mutationsTypes.DESELECT_PRODUCT_SUCCESS,
                {
                    products: cart.products,
                    totalPrice: cart.total_price
                }    
            )
        },
        errorCallback (errorResponse) {
            const errors = errorResponse.data.error.details

            commit(
                mutationsTypes.DESELECT_PRODUCT_FAILURE,
                errors
            )
        }
    })
}

function createCheckoutSession ({ commit }) {
    commit(mutationsTypes.CREATE_CHECKOUT_SESSION_REQUEST)
    
    checkoutSessionService.createSession(null, {
        successCallback () {
            commit(mutationsTypes.CREATE_CHECKOUT_SESSION_SUCCESS)
        },
        errorCallback (errorResponse) {
            const errors = errorResponse.data.error.details
            
            commit(
                mutationsTypes.CREATE_CHECKOUT_SESSION_FAILURE,
                errors
            )
        }
    })
}

export const actionsTypes = {
    SAVE_CART: 'SAVE_CART',
    REMOVE_PRODUCT: 'REMOVE_PRODUCT',
    SELECT_PRODUCT: 'SELECT_PRODUCT',
    DESELECT_PRODUCT: 'DESELECT_PRODUCT',
    CREATE_CHECKOUT_SESSION: 'CREATE_CHECKOUT_SESSION'
}

const actions = {
    [actionsTypes.SAVE_CART]: saveCart,
    [actionsTypes.REMOVE_PRODUCT]: removeProduct,
    [actionsTypes.SELECT_PRODUCT]: selectProduct,
    [actionsTypes.DESELECT_PRODUCT]: deselectProduct,
    [actionsTypes.CREATE_CHECKOUT_SESSION]: createCheckoutSession
}

export default actions