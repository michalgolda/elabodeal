<template>
	<BaseView>
		<div class="wrapper success-msg-wrapper flex-center">
			<div class="success-msg">
				<h1 class="success-msg__title">
					{{ paymentFirstName }}, dziękujemy za zakupy 😉
				</h1>
				<h3 class="success-msg__description">
					Płatność zakończona sukcesem. Wkrótce otrzymasz wiadomość na 
					<span class="success-msg__highlight">{{ deliveryEmail }}</span> z zakupionym produktem. Możesz opuścić widoczną stronę, klikając w przycisk poniżej.
				</h3>
				<a 
					class="btn btn__primary" 
					href="/"
				>
					Strona główna
				</a>
			</div>
		</div>
	</BaseView>
</template>
<script>
import { createNamespacedHelpers } from 'vuex';

import BaseView from './BaseView';

const { mapState: mapPaymentState } = createNamespacedHelpers('payment');
const { mapState: mapDeliverState } = createNamespacedHelpers('deliver');

export default {
	components: {
		BaseView
	},
	computed: {
		...mapPaymentState({
			paymentFirstName: state => state.payment.first_name
		}),
		...mapDeliverState({
			deliveryEmail: state => state.delivery.email
		})
	}
}
</script>