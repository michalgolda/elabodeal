import { uiModuleTypes } from './ui'
import { getApplicationData } from '@/utils/data'
import { createNamespacedTypes } from '@/utils/store'
import { cartService, checkoutSessionService } from '@/services'


const state = () => {
    const { products } = getApplicationData()

    const selectedProducts = products.filter((product) => {
        return product.selected === true
    })

    return {
        products,
        selectedProducts
    }
}

const mutationTypes = {
    REMOVE_PRODUCT: 'REMOVE_PRODUCT',
    SELECT_PRODUCT: 'SELECT_PRODUCT',
    DESELECT_PRODUCT: 'DESELECT_PRODUCT',
    UPDATE_TOTAL_PRICE: 'UPDATE_TOTAL_PRICE',
    UPDATE_PRODUCT_COUNT: 'UPDATE_PRODUCT_COUNT',
    ADD_PRODUCT_PRICE_TO_TOTAL_PRICE: 'ADD_PRODUCT_PRICE_TO_TOTAL_PRICE',
    SUBTRACT_PRODUCT_PRICE_FROM_TOTAL_PRICE: 'SUBTRACT_PRODUCT_PRICE_FROM_TOTAL_PRICE'
}

const mutations = {
    [mutationTypes.REMOVE_PRODUCT] (state, productId) {
        state.products = state.products.filter((product) => {
            return product.id !== productId
        })
    },
    [mutationTypes.SELECT_PRODUCT] (state, productId) {
        const product = state.products.find((product) => {
            return product.id === productId
        })

        state.selectedProducts.push(product)
    },
    [mutationTypes.DESELECT_PRODUCT] (state, productId) {
        state.selectedProducts = state.selectedProducts.filter((product) => {
            return product.id !== productId
        })
    },
    [mutationTypes.ADD_PRODUCT_PRICE_TO_TOTAL_PRICE] (state, productId) {
        const product = state.products.find((product) => {
            return product.id === productId
        })

        const totalPriceElm = document.getElementsByClassName('cart-total-price')[1]
    
        const updatedTotalPrice = parseFloat(totalPriceElm.innerText) + product.price

        totalPriceElm.innerText = updatedTotalPrice.toFixed(2)
    },
    [mutationTypes.SUBTRACT_PRODUCT_PRICE_FROM_TOTAL_PRICE] (state, productId) {
        const product = state.products.find((product) => {
            return product.id === productId
        })

        const totalPriceElm = document.getElementsByClassName('cart-total-price')[1]
    
        const updatedTotalPrice = parseFloat(totalPriceElm.innerText) - product.price

        totalPriceElm.innerText = updatedTotalPrice.toFixed(2)
    },
    [mutationTypes.UPDATE_TOTAL_PRICE] (_, totalPrice) {
        const totalPriceElms = document.getElementsByClassName('cart-total-price')
    
        totalPriceElms[0].innerHTML = totalPrice
        totalPriceElms[1].innerHTML = totalPrice
    },
    [mutationTypes.UPDATE_PRODUCT_COUNT] (_, productCount) {
        const productCountElm = document.getElementById('cart-product-count')
    
        productCountElm.innerHTML = `(${productCount})`

        document.title = `Elabodeal - Koszyk (${productCount})`
    }
}

const getterTypes = {
    GET_PRODUCTS: 'GET_PRODUCTS',
    CART_IS_EMPTY: 'CART_IS_EMPTY',
    CREATE_CHECKOUT_SESSION_BTN_ENABLED: 'CREATE_CHECKOUT_SESSION_BTN_ENABLED'
}

const getters = {
    [getterTypes.GET_PRODUCTS] (state) {
        return state.products
    },
    [getterTypes.CART_IS_EMPTY] (state) {
        return state.products.length === 0
    },
    [getterTypes.CREATE_CHECKOUT_SESSION_BTN_ENABLED] (state) {
        return state.selectedProducts.length > 0 && state.products.length > 0
    }
}

const actionTypes = {
    SAVE_CART: 'SAVE_CART',
    TOGGLE_PRODUCT: 'TOGGLE_PRODUCT',
    CREATE_CHECKOUT_SESSION: 'CREATE_CHECKOUT_SESSION',
    REMOVE_PRODUCT_FROM_CART: 'REMOVE_PRODUCT_FROM_CART'
}

const actions = {
    [actionTypes.SAVE_CART] (ctx, { title, description }) {
        const data = new FormData()

        data.append('title', title)
        data.append('description', description)

        cartService.save(data, {
            successCallback: () => {
                this.$modalManager.hide()
            },
            errorCallback: (errorRes) => {
                ctx.commit(
                    uiModuleTypes.mutations.SHOW_ERRORS,
                    errorRes.data.error.details,
                    { root: true }
                )
            }
        })
    },
    [actionTypes.REMOVE_PRODUCT_FROM_CART] (ctx, { productId }) {
        const data = new FormData()

        data.append('product_id', productId)

        cartService.removeProduct({ data }, {
            successCallback: ({ data }) => {
                const { cart } = data

                ctx.commit(
                    mutationTypes.REMOVE_PRODUCT,
                    productId,
                    { root: true }
                )

                ctx.commit(
                    mutationTypes.UPDATE_TOTAL_PRICE,
                    cart.total_price,
                    { root: true }
                )

                ctx.commit(
                    mutationTypes.UPDATE_PRODUCT_COUNT,
                    cart.product_count,
                    { root: true }
                )
            }
        });
    },
    [actionTypes.TOGGLE_PRODUCT] (ctx, { productId, selected }) {
        const data = new FormData()

        data.append('product_id', productId)

        cartService.selectOrDeselectProduct(data, {
            successCallback: () => {
                const actionType = selected ? 'SELECT' : 'UNSELECT'

                switch (actionType) {
                    case 'SELECT':
                        ctx.commit(
                            mutationTypes.SELECT_PRODUCT, 
                            productId,
                            { root: true }
                        )
                        
                        ctx.commit(
                            mutationTypes.ADD_PRODUCT_PRICE_TO_TOTAL_PRICE,
                            productId,
                            { root: true }
                        )

                        break
                    case 'UNSELECT':
                        ctx.commit(
                            mutationTypes.DESELECT_PRODUCT, 
                            productId,
                            { root: true }
                        )

                        ctx.commit(
                            mutationTypes.SUBTRACT_PRODUCT_PRICE_FROM_TOTAL_PRICE,
                            productId,
                            { root: true }
                        )

                        break
                }
            }
        })
    },
    [actionTypes.CREATE_CHECKOUT_SESSION] () {
        checkoutSessionService.createSession(null, {
            successCallback: () => {
                window.location = '/cart/checkout/'
            }
        })
    }
}

export const mainModuleTypes = createNamespacedTypes('main', {
    getters: getterTypes,
    actions: actionTypes,
    mutations: mutationTypes
})

const mainModule = {
    state,
    actions,
    getters,
    mutations,
    namespaced: true
}

export default mainModule