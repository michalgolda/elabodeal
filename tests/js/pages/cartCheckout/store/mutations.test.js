import mutations, { mutationsTypes } from '@/pages/cartCheckout/store/mutations'


describe('SUCCEED_CHECKOUT_SESSION', () => {
    test(mutationsTypes.SUCCEED_CHECKOUT_SESSION_REQUEST, () => {
        const state = { loading: false }

        mutations[mutationsTypes.SUCCEED_CHECKOUT_SESSION_REQUEST](state)

        expect(state).toStrictEqual({ loading: true })
    })

    test(mutationsTypes.SUCCEED_CHECKOUT_SESSION_SUCCESS, () => {
        const state = { 
            loading: true, 
            currentStep: '',
            payerFirstName: ''
        }


        mutations[mutationsTypes.SUCCEED_CHECKOUT_SESSION_SUCCESS](state, {
            firstName: 'test'
        })

        expect(state).toStrictEqual({
            loading: false,
            currentStep: 'success',
            payerFirstName: 'test'
        })
    })

    test(mutationsTypes.SUCCEED_CHECKOUT_SESSION_FAILURE, () => {
        const state = { loading: true, errors: {} }

        mutations[mutationsTypes.SUCCEED_CHECKOUT_SESSION_FAILURE](state, {
            test: 'test'
        })

        expect(state).toStrictEqual({
            loading: false,
            errors: { test: 'test' }
        })
    })
})

describe('CANCEL_CHECKOUT_SESSION', () => {
    test(mutationsTypes.CANCEL_CHECKOUT_SESSION_REQUEST, () => {
        const state = { loading: false }

        mutations[mutationsTypes.CANCEL_CHECKOUT_SESSION_REQUEST](state)

        expect(state).toStrictEqual({ loading: true })
    })

    test(mutationsTypes.CANCEL_CHECKOUT_SESSION_SUCCESS, () => {
        const state = { loading: true }

        delete window.location

        window.location = { assign: jest.fn() }

        mutations[mutationsTypes.CANCEL_CHECKOUT_SESSION_SUCCESS](state)

        expect(state).toStrictEqual({ loading: false })

        expect(window.location.assign).toHaveBeenCalledWith('/cart/')
    })

    test(mutationsTypes.CANCEL_CHECKOUT_SESSION_FAILURE, () => {
        const state = { loading: true, errors: {} }

        mutations[mutationsTypes.CANCEL_CHECKOUT_SESSION_FAILURE](state, {
            test: 'test'
        })

        expect(state).toStrictEqual({
            loading: false,
            errors: { test: 'test' }
        })
    })
})

describe('UPDATE_CHECKOUT_SESSION', () => {
    test(mutationsTypes.UPDATE_CHECKOUT_SESSION_REQUEST, () => {
        const state = { loading: false }

        mutations[mutationsTypes.UPDATE_CHECKOUT_SESSION_REQUEST](state)

        expect(state).toStrictEqual({ loading: true })
    })

    test(mutationsTypes.UPDATE_CHECKOUT_SESSION_SUCCESS, () => {
        const state = { 
            loading: true,
            currentStep: '',
            delivery: {} 
        }

        mutations[mutationsTypes.UPDATE_CHECKOUT_SESSION_SUCCESS](state, {
            email: 'test',
            firstName: 'test',
            lastName: 'test'
        })

        expect(state).toStrictEqual({ 
            loading: false,
            currentStep: 'payment',
            delivery: { 
                firstName: 'test', 
                lastName: 'test', 
                email: 'test' 
            }
        })
    })

    test(mutationsTypes.UPDATE_CHECKOUT_SESSION_FAILURE, () => {
        const state = { loading: true, errors: {} }

        mutations[mutationsTypes.UPDATE_CHECKOUT_SESSION_FAILURE](state, {
            test: 'test'
        })

        expect(state).toStrictEqual({
            loading: false,
            errors: { test: 'test' }
        })
    })
})

test(mutationsTypes.SET_CURRENT_STEP, () => {
    const state = { currentStep: '' }

    mutations[mutationsTypes.SET_CURRENT_STEP](state, 'deliver')

    expect(state).toStrictEqual({ currentStep: 'deliver' })
})