<template>
	<BaseView>
		<div class="form-wrapper">
			<form 
				@submit.prevent="handleSubmit" 
				class="form"
				autocomplete="off" 
			>
				<div class="form__section">
					<div>
						<label>IMIĘ</label>
						<p
							class="form__input-error-msg"
							v-for="error in firstNameErrors"
							:key="error"
						>
							{{ error }}
						</p>
						<input 
							name="first_name"
							type="text"
							required="required"
							:value="first_name"
							ref="first_name"
						>
					</div>
					<div>
						<label>NAZWISKO</label>
						<p
							class="form__input-error-msg"
							v-for="error in lastNameErrors"
							:key="error"
						>
							{{ error }}
						</p>
						<input 
							name="last_name"
							type="text"
							required="required"
							:value="last_name"
							ref="last_name" 
						>
					</div>
				</div>
				<div>
					<label>E-MAIL</label>
					<p
						class="form__input-error-msg"
						v-for="error in emailErrors"
						:key="error"
					>
						{{ error }}
					</p>
					<input 
						name="email"
						type="email"
						required="required"
						:value="email"
						ref="email" 
					>
				</div>
				<button 
					class="btn btn__primary btn-block"
					type="submit" 
				>
					Przejdź dalej
				</button>
				<button 
					class="btn btn__secondary btn-block"
					type="button"
					@click="() => cancelCheckoutProcess()"
				>
					Wstecz
				</button>
			</form>
		</div>
	</BaseView>
</template>
<script>
import { 
	createNamespacedHelpers,
	mapState as mapRootState,
	mapActions as mapRootActions } from 'vuex';

import BaseView from './BaseView';

const { mapState: mapUiState } = createNamespacedHelpers('ui');
const { mapActions: mapDeliverActions } = createNamespacedHelpers('deliver');


export default {
	components: {
		BaseView
	},
	computed: {
		...mapUiState({
			firstNameErrors: state => state.error.first_name,
			lastNameErrors: state => state.error.last_name,
			emailErrors: state => state.error.email
		}),
		...mapRootState(['email', 'first_name', 'last_name'])
	},
	methods: {
		...mapRootActions(['cancelCheckoutProcess']),
		...mapDeliverActions(['collectDeliverData']),
		handleSubmit () {
			const { first_name, last_name, email } = this.$refs;

			this.collectDeliverData({
				email: email.value,
				last_name: last_name.value,
				first_name: first_name.value
			});
		}
	}
}
</script>