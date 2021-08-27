import getters from '../../../../../elabodeal/web/static/js/pages/cart/store/getters'


test('getSelectedProducts', () => {
    const state = { products: [{ selected: true }] }

    const result = getters.getSelectedProducts(state)

    expect(result).toStrictEqual([{ selected: true }])
})