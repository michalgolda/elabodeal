import alert from '../../alert';


export default class PaymentFormUIComponent {
    constructor() {
        this.elements = this.loadElements();
        this.constants = this.loadConstants();
        this.dependencies = this.loadDependencies();
        this.handlers = this.loadHandlers();

        this.bindUIElements();
        this.bindUIActions();
    }

    bindUIElements() {
        var cardElement = this.dependencies.stripeElements.create( 'card', {
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
        } );

        cardElement.mount( this.elements.cardElementContainer );

        this.elements[ 'cardElement' ] = cardElement;
    }

    bindUIActions() {
        this.elements.form.submit( this.handlers.handleSubmitPayment );
    }

    loadHandlers() {
        return {
            handleSubmitPayment: ( e ) => {
                e.preventDefault();

                var formData = this.elements.form.serializeArray();
                var actionURL = this.elements.form.attr( 'action' );

                $.ajax( {
                    url: actionURL,
                    method: 'POST',
                    headers: {
                        'X-CSRFtoken': this.constants.csrfToken
                    },
                    data: formData,
                    success: ( result ) => {
                        var data = result.data;
                  
                        var clientSecret = data.client_secret;

                        var payerData = JSON.parse( data.metadata.payer );
                        var billingDetailsData = { 
                            name: `${ payerData.first_name } ${ payerData.last_name }`,
                            phone: payerData.phone_number,
                            email: payerData.email
                        };

                        this.handlers.handleConfirmCardPayment( clientSecret, billingDetailsData  );
                    },
                    error: () => {
                        alert( 'Coś poszło nie tak. Spróbuj ponownie.', 'error' );
                    }
                } );
            },
            handleConfirmCardPayment: ( clientSecret, billingDetailsData ) => {
                this.dependencies.stripe
                    .confirmCardPayment( clientSecret, {
                        payment_method: {
                            card: this.elements.cardElement,
                            billing_details: billingDetailsData
                        }
                    } )
                    .then( ( result ) => {
                        if ( result.paymentIntent )
                            window.location = this.elements.form.attr( 'success-url' );
                        else alert( 'Coś poszło nie tak. Spróbuj ponownie.', 'error' );
                    } )
            }
        }
    }

    loadConstants() {
        return {
            csrfToken: $( 'meta[name="csrf_token"]' ).attr( 'content' ),
            stripePublicKey: $( 'meta[name="stripe_public_key"]' ).attr( 'content' )
        }
    }

    loadDependencies() {
        var stripe = Stripe( this.constants.stripePublicKey );
        var stripeElements = stripe.elements();

        return {
            stripe: stripe,
            stripeElements: stripeElements
        }
    }

    loadElements() {
        return {
            form: $( '#js-payment' ),
            cardElementContainer: $( '#card-element' )[ 0 ]
        }
    }
} 