<template>
	<Modal
		title="Zapisywanie koszyka"
	>
		<form 
			autocomplete="off"
			@submit.prevent="saveCart"
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
					ref="titleInputRef"
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
					ref="descriptionInputRef"
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
import { computed, ref } from 'vue'
import { useStore } from 'vuex'

import { actionsTypes } from '../store/actions'

import Modal from '@/components/Modal'


export default {
	components: {
		Modal
	},
	setup () {
		const store = useStore()

		const titleInputRef = ref(null)
		const descriptionInputRef = ref(null)

		const saveCart = () => {
			const titleInput = titleInputRef.value
			const descriptionInput = descriptionInputRef.value

			store.dispatch(
				actionsTypes.SAVE_CART,
				{ 
					title: titleInput.value, 
					description: descriptionInput.value
				}
			)
		}

		const titleErrors = computed(() => {
			return store.state.errors.title
		})

		const descriptionErrors = computed(() => {
			return store.state.errors.description
		})

		return {
			saveCart,
			titleErrors,
			titleInputRef,
			descriptionErrors,
			descriptionInputRef
		}
	}
}
</script>