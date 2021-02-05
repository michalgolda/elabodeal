import Alert from '../../alert';
import { ALERT_MESSAGES } from '../../constants';

import httpClient from '../../utils/httpClient';

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

                var actionURL = this.elements.form.attr( 'action' );
                var formData = new FormData( this.elements.form.get( 0 ) );
                var data = Object.fromEntries( formData );

                httpClient.post( actionURL, data )
                    .then( response => {
                        var data = response.data;
                  
                        var clientSecret = data.client_secret;

                        var payerData = JSON.parse( data.metadata.payer );
                        var billingDetailsData = { 
                            name: `${ payerData.first_name } ${ payerData.last_name }`,
                            phone: payerData.phone_number,
                            email: payerData.email
                        };

                        this.handlers.handleConfirmCardPayment( clientSecret, billingDetailsData  );
                    } )
                    .catch( error => {
                        if ( error.response )
                            Alert.error( ALERT_MESSAGES.SERVER_ERROR );
                    } )
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
                        else Alert.error( ALERT_MESSAGES.SERVER_ERROR );
                    } )
            }
        }
    }

    loadConstants() {
        return {
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