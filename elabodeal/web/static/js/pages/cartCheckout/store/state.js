import { getApplicationData } from '@/utils/data'


function state () {
    const {
        delivery,
		checkout_session: checkoutSession,
		summary_products: summaryProducts,
		summary_total_price: summaryTotalPrice,
		stripe_publishable_key: stripePublishableKey 
    } = getApplicationData()

    const {
        step: currentStep,
        cs: paymentIntentClientSecret 
    } = checkoutSession

    return {
        errors: {},
        loading: false,
        summaryProducts,
		summaryTotalPrice,
        payerFirstName: '',
		stripePublishableKey,
		paymentIntentClientSecret,
        delivery: delivery ? {
            email: delivery.email,
            firstName: delivery.first_name,
            lastName: delivery.last_name
        } : {},
        currentStep: currentStep ? currentStep : 'deliver'
    }
}

export default state