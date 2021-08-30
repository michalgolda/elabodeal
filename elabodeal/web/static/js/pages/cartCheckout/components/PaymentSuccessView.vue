<template>
	<BaseView>
		<div class="wrapper success-msg-wrapper flex-center">
			<div class="success-msg">
				<h1 class="success-msg__title">
					{{ firstName }}, dziękujemy za zakupy 😉
				</h1>
				<h3 class="success-msg__description">
					Płatność zakończona sukcesem. Wkrótce otrzymasz wiadomość na 
					<span class="success-msg__highlight">{{ email }}</span> z zakupionym produktem. Możesz opuścić widoczną stronę, klikając w przycisk poniżej.
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
import { computed } from 'vue'
import { useStore } from 'vuex'

import BaseView from './BaseView';


export default {
	components: {
		BaseView
	},
	setup () {
		const store = useStore()

		const firstName = computed(() => {
			return store.state.payerFirstName
		})

		const email = computed(() => {
			return store.state.delivery.firstName
		})

		return {
			email,
			firstName
		}
	}
}
</script>