( function( window, document ) {
	document.addEventListener( 'DOMContentLoaded', function() {
		var paymentForm = document.getElementById( 'payment-form' );

		if (!paymentForm) {
			return;
		}

		var stripe = Stripe( window.__stripe_public_key__ );
		var elements = stripe.elements();

		var errorBox = $( '#payment-error-msg' );

		var card = elements.create( 'card', {
		  style: {
		    base: {
		      color: '#011627',
		      fontWeight: 500,
		      fontFamily: 'Montserrat, Open Sans, Segoe UI, sans-serif',
		      fontSize: '15.5px'
		    },
		    invalid: {
		      iconColor: '#E71D36',
		      color: '#E71D36',
		    },
		  },
		});

		card.mount( '#card-element' );

		paymentForm.addEventListener( 'submit', function( e ) {
			e.preventDefault();

			var formData = new $( '#payment-form' ).serializeArray();

			fetch( '/api/payments/', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json',
					'X-CSRFToken': window.__csrf_token__
				},
				body: JSON.stringify({
					'first_name': formData[0]['value'],
					'last_name': formData[1]['value'],
					'email': formData[2]['value'],
					'phone_number': formData[3]['value'],
				})
			})
			.then( res => {
				if ( res.ok ) {
					const data = res.json()
						.then( data => {
							var billingDetails = {
								'name': `${data.metadata.first_name} ${data.metadata.last_name}`,
								'phone': data.metadata.phone_number,
								'email': data.metadata.email
							}

							var clientSecret = data.client_secret

							stripe
								.confirmCardPayment( clientSecret, {
									payment_method: {
										card: card,
										billing_details: billingDetails
									}
								})
								.then( function( result ) {
									if ( result.paymentIntent ) {
										var url = `${window.location.origin}/success/`;
										window.location = url;
									} else {
										var errorCode = result.error.code;
										
										var displayErrorMsg = 'Autoryzacja płatności zakończyła się niepowodzeniem. Spróbuj ponownie';

										if ( errorCode === 'payment_intent_authentication_failure' ) {
											errorBox.html( displayErrorMsg );
										} else {
											var paymentIntentId = result.error.payment_intent.id;
											var errorMsg = result.error.message;

											Sentry.configureScope( function( scope ) {
											  scope.setFingerprint('Payment-proccess');
											  scope.setTag(
											  	'payment_intent_id', 
											  	paymentIntentId
											  );
											});

											Sentry.captureException( new Error( errorMsg ) );
										}
									}
								})
						})
				} else {
					var statusText = result.statusText;
					var displayErrorMsg = 'Coś poszło nie tak. Przepraszamy za utrdunienia';

					errorBox.html( displayErrorMsg );

					Sentry.configureScope( function( scope ) {
					  scope.setFingerprint( 'Payment-proccess' );
					});
					Sentry.captureException (new Error( statusText ) );
				}
			});
		});
	});
})( window, document );