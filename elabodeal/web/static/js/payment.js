( function( document, window, jquery, constants ){
	document.addEventListener( 'DOMContentLoaded', function(){
		var form = document.getElementById( constants.FORM_ID );

		if ( !form ) return;

		var stripe = Stripe( window.__stripe_public_key__ );
		var stripe_elements = stripe.elements();

		var card = stripe_elements.create( 'card', {
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
		} );

		card.mount( `#${constants.CARD_ELEMENT_ID}` );

		form.addEventListener( 'submit', function( e ){
			e.preventDefault();

			const formData = $( this ).serializeArray();
			
			jquery.ajax( {
				method: 'POST',
				url: constants.PAYMENT_INIT_ACTION_URL,
				headers: {
					'X-CSRFToken': constants.CSRF_TOKEN
				},
				data: formData,
				success: successHandler = ( result ) => {
					const data = result.data;

					const payer = JSON.parse(data.metadata.payer);
					const billingDetails = {'name': `${payer.first_name} ${payer.last_name}`,
											'phone': payer.phone_number,
											'email': payer.email};

					var clientSecret = data.client_secret;

					stripe
						.confirmCardPayment( clientSecret, {
							payment_method: {
								card: card,
								billing_details: billingDetails
							}
						} )
						.then( function( result ){
							if ( result.paymentIntent ){
								var redirect_url = `${window.location.href}success/`;

								window.location = redirect_url;
							} else {
								console.error( result );
							}
						} )
				},
				error: errorHandler = ( e ) => {
					console.error( e );
				}
			} );
		} );
	} );
} )( document, window, $, {
	'FORM_ID': 'payment-form',
	'CARD_ELEMENT_ID': 'card-element',
	'PAYMENT_INIT_ACTION_URL': window.__actionUrls__['payment-init'],
	'CSRF_TOKEN': window.__csrf_token__
});