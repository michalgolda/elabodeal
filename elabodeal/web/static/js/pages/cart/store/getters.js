const getSelectedProducts = (state) => {
    return state.products.filter((product) => {
        return product.selected === true
    })
}

const getters = { getSelectedProducts }

export default getters