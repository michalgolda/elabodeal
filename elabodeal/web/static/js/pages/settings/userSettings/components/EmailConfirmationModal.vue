<template>
	<modal title="Weryfikacja adresu email">
		<email-confirmation-form
			:confirmAction="confirmAction"
			:resendAction="resendAction"
			:email="email"
			@success="handleSuccess"
		/>
	</modal>
</template>
<script>
import Modal from '../../../../components/Modal.vue';
import EmailConfirmationForm from '../../../../components/EmailConfirmationForm.vue';


export default {
	components: {
		Modal,
		EmailConfirmationForm
	},
	methods: {
		handleSuccess() {
			this.$modal.hide();
			
			window.location.reload();
		}
	}
}
</script>