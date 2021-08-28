const getSelectedProducts = (state) => {
    return state.products.filter((product) => {
        return product.selected === true
    })
}

export const gettersTypes = {
    GET_SELECTED_PRODUCTS: 'GET_SELECTED_PRODUCTS'
}

const getters = { 
    [gettersTypes.GET_SELECTED_PRODUCTS]: getSelectedProducts 
}

export default getters