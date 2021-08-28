import getters from '../../../../../elabodeal/web/static/js/pages/cart/store/getters'
import { gettersTypes } from '../../../../../elabodeal/web/static/js/pages/cart/store/getters'


test(gettersTypes.GET_SELECTED_PRODUCTS, () => {
    const state = { products: [{ selected: true }] }

    const result = getters[gettersTypes.GET_SELECTED_PRODUCTS](state)

    expect(result).toStrictEqual([{ selected: true }])
})