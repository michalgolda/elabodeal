<template>
	<div class="modal-wrapper flex-center">
		<div class="modal">
			<div class="modal__header">
				<p class="modal__title">
					{{ title }}
				</p>
				<i 
					class="fas fa-times modal__close-btn"
					@click="$modalManager.hide()"
				/>
			</div>
			<div class="modal__body">
				<slot />
			</div>
		</div>
	</div>
</template>
<script>
export default {
	props: {
		title: {
			type: String,
			required: true
		}
	}
}
</script>