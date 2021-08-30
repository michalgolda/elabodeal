import { mutationsTypes } from './mutations'
import { checkoutSessionService } from '@/services'


function succeedCheckoutSession ({ commit }, { firstName }) {
    commit(mutationsTypes.SUCCEED_CHECKOUT_SESSION_REQUEST)
    
    checkoutSessionService.succeedSession(null, {
        successCallback () {
            commit(mutationsTypes.SUCCEED_CHECKOUT_SESSION_SUCCESS, {
                firstName
            })
        },
        errorCallback (errorResponse) {
            const errors = errorResponse.data.error.details

            commit(
                mutationsTypes.SUCCEED_CHECKOUT_SESSION_FAILURE, 
                errors
            )
        }
    })
}

function cancelCheckoutSession ({ commit }) {
    commit(mutationsTypes.CANCEL_CHECKOUT_SESSION_REQUEST)

    checkoutSessionService.removeSession(null, {
        successCallback () {
            commit(mutationsTypes.CANCEL_CHECKOUT_SESSION_SUCCESS)
        },
        errorCallback (errorResponse) {
            const errors = errorResponse.data.error.details

            commit(mutationsTypes.CANCEL_CHECKOUT_SESSION_FAILURE, errors)
        }
    })
}

function updateCheckoutSession ({ commit }, { firstName, lastName, email }) {
    const data = new FormData()

    data.append('email', email)
    data.append('last_name', lastName)
    data.append('first_name', firstName)

    commit(mutationsTypes.UPDATE_CHECKOUT_SESSION_REQUEST)

    checkoutSessionService.updateSession(data, {
        successCallback ({ data }) {
            const { delivery } = data

            const { 
                email,
                firstName,
                lastName } = delivery

            commit(mutationsTypes.UPDATE_CHECKOUT_SESSION_SUCCESS, {
                email,
                firstName,
                lastName
            })
        },
        errorCallback (errorResponse) {
            const errors = errorResponse.data.error.details

            commit(mutationsTypes.UPDATE_CHECKOUT_SESSION_FAILURE, errors)
        }
    })
}

export const actionsTypes = {
    SUCCEED_CHECKOUT_SESSION: 'SUCCEED_CHECKOUT_SESSION',
    CANCEL_CHECKOUT_SESSION: 'CANCEL_CHECKOUT_SESSION',
    UPDATE_CHECKOUT_SESSION: 'UPDATE_CHECKOUT_SESSION'
}

const actions = {
    [actionsTypes.SUCCEED_CHECKOUT_SESSION]: succeedCheckoutSession,
    [actionsTypes.CANCEL_CHECKOUT_SESSION]: cancelCheckoutSession,
    [actionsTypes.UPDATE_CHECKOUT_SESSION]: updateCheckoutSession
}

export default actions
