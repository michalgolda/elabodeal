<template>
	<Modal
		title="Zapisywanie koszyka"
	>
		<form 
			autocomplete="off"
			@submit.prevent="handleSubmit"
		>
			<div>
				<label>TYTUŁ</label>
				<p
					class="form__input-error-msg"
					v-for="error in titleErrors"
					:key="error"
				>
					{{ error }}
				</p>
				<input 
					type="text" 
					name="title" 
					required
					@change="handleChangeTitle"
				>
			</div>
			<div style="margin-top: .5rem; margin-bottom: .5rem;">
				<label>OPIS</label>
				<p
					class="form__input-error-msg"
					v-for="error in descriptionErrors"
					:key="error"
				>
					{{ error }}
				</p>
				<textarea 
					name="description" 
					@change="handleChangeDescription"
				/> 
			</div>
			<button 
				class="btn btn__secondary-outline btn-block"
			>
				Zapisz koszyk
			</button>
		</form>
	</Modal>
</template>
<script>
import { 
	mapActions as mapRootActions,
	createNamespacedHelpers } from 'vuex';

import Modal from '@/components/Modal';


const { mapState: mapUiState } = createNamespacedHelpers('ui');


export default {
	components: {
		Modal
	},
	computed: mapUiState({
		titleErrors: state => state.error.title,
		descriptionErrors: state => state.error.description
	}),
	data () {
		return {
			title: '',
			description: ''
		}
	},
	methods: {
		...mapRootActions(['saveCart']),
		handleSubmit () {
			this.saveCart({
				title: this.title,
				description: this.description
			});
		},
		handleChangeTitle (e) {
			this.title = e.target.value;
		},
		handleChangeDescription (e) {
			this.description = e.target.value;
		}
	}
}
</script>