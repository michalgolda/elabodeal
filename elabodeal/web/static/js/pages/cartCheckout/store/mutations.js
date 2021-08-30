function succeedCheckoutSessionRequest (state) { state.loading = true }
function succeedCheckoutSessionSuccess (state, { firstName }) {
    state.loading = false
    state.currentStep = 'success'
    state.payerFirstName = firstName
}
function succeedCheckoutSessionFailure (state, errors) {
    state.loading = false
    state.errors = errors
}


function cancelCheckoutSessionRequest (state) { state.loading = true }
function cancelCheckoutSessionSuccess (state) {
    state.loading = false

    window.location.assign('/cart/')
}
function cancelCheckoutSessionFailure (state, errors) {
    state.loading = false
    state.errors = errors
}


function updateCheckoutSessionRequest (state) { state.loading = true }
function updateCheckoutSessionSuccess (state, { firstName, lastName, email }) {
    state.loading = false
    state.currentStep = 'payment'
    state.delivery = { firstName, lastName, email }
}
function updateCheckoutSessionFailure (state, errors) {
    state.loading = false
    state.errors = errors
}


function setCurrentStep (state, step) { state.currentStep = step }


export const mutationsTypes = {
    SUCCEED_CHECKOUT_SESSION_REQUEST: 'SUCCEED_CHECKOUT_SESSION_REQUEST',
    SUCCEED_CHECKOUT_SESSION_SUCCESS: 'SUCCEED_CHECKOUT_SESSION_SUCCESS',
    SUCCEED_CHECKOUT_SESSION_FAILURE: 'SUCCEED_CHECKOUT_SESSION_FAILURE',

    CANCEL_CHECKOUT_SESSION_REQUEST: 'CANCEL_CHECKOUT_SESSION_REQUEST',
    CANCEL_CHECKOUT_SESSION_SUCCESS: 'CANCEL_CHECKOUT_SESSION_SUCCESS',
    CANCEL_CHECKOUT_SESSION_FAILURE: 'CANCEL_CHECKOUT_SESSION_FAILURE',

    UPDATE_CHECKOUT_SESSION_REQUEST: 'UPDATE_CHECKOUT_SESSION_REQUEST',
    UPDATE_CHECKOUT_SESSION_SUCCESS: 'UPDATE_CHECKOUT_SESSION_SUCCESS',
    UPDATE_CHECKOUT_SESSION_FAILURE: 'UPDATE_CHECKOUT_SESSION_FAILURE',

    SET_CURRENT_STEP: 'SET_CURRENT_STEP'
}

const mutations = {
    [mutationsTypes.SUCCEED_CHECKOUT_SESSION_REQUEST]: succeedCheckoutSessionRequest,
    [mutationsTypes.SUCCEED_CHECKOUT_SESSION_SUCCESS]: succeedCheckoutSessionSuccess,
    [mutationsTypes.SUCCEED_CHECKOUT_SESSION_FAILURE]: succeedCheckoutSessionFailure,

    [mutationsTypes.CANCEL_CHECKOUT_SESSION_REQUEST]: cancelCheckoutSessionRequest,
    [mutationsTypes.CANCEL_CHECKOUT_SESSION_SUCCESS]: cancelCheckoutSessionSuccess,
    [mutationsTypes.CANCEL_CHECKOUT_SESSION_FAILURE]: cancelCheckoutSessionFailure,

    [mutationsTypes.UPDATE_CHECKOUT_SESSION_REQUEST]: updateCheckoutSessionRequest,
    [mutationsTypes.UPDATE_CHECKOUT_SESSION_SUCCESS]: updateCheckoutSessionSuccess,
    [mutationsTypes.UPDATE_CHECKOUT_SESSION_FAILURE]: updateCheckoutSessionFailure,

    [mutationsTypes.SET_CURRENT_STEP]: setCurrentStep
}

export default mutations