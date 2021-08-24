import { onMounted, ref } from 'vue'
import Alert from '@/alert'


export default function useStripe (
    publishableKey, 
    paymentIntentClientSecret,
    { paymentSuccessCallback, paymentErrorCallback }
) {
    // eslint-disable-next-line 
    const stripe = new Stripe(publishableKey)
    const stripeElements = stripe.elements()

    const defaultElementOptions = {
        style: {
            base: {
                color: '#011627',
                fontWeight: 500,
                fontFamily: 'Montserrat, Open Sans, Segoe UI, sans-serif',
                fontSize: '15.5px'
            },
            invalid: {
                iconColor: '#E71D36',
                color: '#E71D36'
            }
        }
    }

    const cardCvcMountElmRef = ref(null)
    const cardNumberMountElmRef = ref(null)
    const cardExpiryMountElmRef = ref(null)

    var cardCvcStripeElm;

    onMounted(() => {
        const cardCvcMountElm = cardCvcMountElmRef.value
        const cardNumberMountElm = cardNumberMountElmRef.value
        const cardExpiryMountElm = cardExpiryMountElmRef.value

        cardCvcStripeElm = stripeElements.create(
            'cardCvc', 
            defaultElementOptions
        )

        const cardNumberStripeElm = stripeElements.create(
            'cardNumber', 
            defaultElementOptions
        )
        const cardExpiryStripeElm = stripeElements.create(
            'cardExpiry', 
            defaultElementOptions
        )

        cardCvcStripeElm.mount(cardCvcMountElm)
        cardNumberStripeElm.mount(cardNumberMountElm)
        cardExpiryStripeElm.mount(cardExpiryMountElm)
    })

    const emailInputRef = ref(null)
    const phoneNumberInputRef = ref(null)
    const lastNameInputRef = ref(null)
    const firstNameInputRef = ref(null)


    const confirmCardPayment = () => {
        const emailInput = emailInputRef.value
        const lastNameInput = lastNameInputRef.value
        const phoneNumberInput = phoneNumberInputRef.value
        const firstNameInput = firstNameInputRef.value

        const paymentMethod = {
            card: cardCvcStripeElm,
            billing_details: {
                email: emailInput.value,
                name: `${firstNameInput.value} ${lastNameInput.value}`,
                phone: phoneNumberInput.value
            }
        }

        return stripe.confirmCardPayment(paymentIntentClientSecret, {
            payment_method: paymentMethod
        })
        .then((result) => {
            const error = result.error
            const paymentIntent = result.paymentIntent
            
            const firstName = firstNameInput.value

            const paymentErrorCallbackWrapper = (error) => {
                const errorType = error.type

                switch (errorType) {
                    case 'validation_error':
                        paymentErrorCallback(error)

                        break
                    default:
                        Alert.info(
                            `Wysątpił błąd podczas 
                            przetwarzania płatności. 
                            Spróbuj ponownie.`
                        )
                }
            }

            error ? (
                paymentErrorCallback && paymentErrorCallbackWrapper(error)
            ) : (
                paymentSuccessCallback && (
                    paymentSuccessCallback(
                        paymentIntent,
                        firstName
                    )
                )
            )
        })
    }
    
    return {
        stripe,
        stripeElements,
        emailInputRef,
        phoneNumberInputRef,
        lastNameInputRef,
        firstNameInputRef,
        confirmCardPayment,
        defaultElementOptions,
        cardCvcMountElmRef,
        cardNumberMountElmRef,
        cardExpiryMountElmRef
    }
}