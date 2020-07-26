var stripe = Stripe(window.__stripe_public_key__);
var elements = stripe.elements();

var card = elements.create('card', {
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

card.mount('#card-element');

var paymentForm = document.getElementById("payment-form");
paymentForm.addEventListener("submit", function(event){
	event.preventDefault();

	var formData = new $('#payment-form').serializeArray();

	fetch('/api/payments/', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
			'X-CSRFToken': window.__csrf_token__
		},
		body: JSON.stringify({
			'first_name': formData[0]['value'],
			'last_name': formData[1]['value'],
			'email': formData[2]['value'],
			'phone_number': formData[3]['value']
		})
	})
	.then(response => {
		if(response.ok) {
			const data = response.json()
				.then(data => {
					stripe
						.confirmCardPayment(data.client_secret, {
							payment_method: {
								card: card,
								billing_details: {
									'name': `${data.metadata.first_name} ${data.metadata.last_name}`,
									'phone': data.metadata.phone_number,
									'email': data.metadata.email
								}
							}
						})
						.then(function(result){
							if(result.paymentIntent) {
								var url = `${window.location.origin}/success/`;
								window.location = url;
							} else {
								if(result.error.code === 'payment_intent_authentication_failure') {
									var displayError = document.getElementById('payment-error-msg');
									displayError.textContent = "Autoryzacja płatności zakończyła się niepowodzeniem. Spróbuj ponownie"
								}
							}
						})
				})
		}
	})
});