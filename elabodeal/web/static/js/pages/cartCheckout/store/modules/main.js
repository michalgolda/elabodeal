import { getApplicationData } from '@/utils/data'
import { checkoutSessionService } from '@/services'
import { createNamespacedTypes } from '@/utils/store'


const state = () => {
    const { 
		user, 
		checkout_session: checkoutSession } = getApplicationData()

	const delivery = checkoutSession['delivery'] ? checkoutSession['delivery'] : {}

	return { 
		first_name: delivery.first_name, 
		last_name: delivery.last_name, 
		email: delivery.email ? delivery.email : user.email 
    }
}

const actionTypes = {
    CANCEL_CHECKOUT_FLOW: 'CANCEL_CHECKOUT_FLOW'
}

const actions = {
    [actionTypes.CANCEL_CHECKOUT_FLOW] () {
        checkoutSessionService.removeSession(null, {
            successCallback: () => {
                window.location = '/cart/'
            }
        })
    }
}

export const mainModuleTypes = createNamespacedTypes('main', {
    actions: actionTypes
})

const mainModule = {
    state,
    actions,
    namespaced: true
}

export default mainModule