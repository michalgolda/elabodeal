<template>
	<Modal
		title="Produkt został dodany do koszyka"
	>
		<div class="cart-updated-item">
			<div class="flex-center">
				<img 
					class="item__cover" 
					:src="product.cover_img_path" 
					:alt="product.title" 
				>
				<div class="item__container">
					<p class="item__title">
						{{ product.title }}
					</p>
					<p class="item__author">
						{{ product.author }}
					</p>
				</div>
			</div>
			<div class="flex-center">
				<p class="item__price">
					{{ product.price }} zł
				</p>
			</div>
		</div>
		<div class="flex-center">
			<a 
				href="/cart/"
				class="btn btn-block btn__secondary" 
				style="margin-right: .5rem;"
				@click="$modalManager.hide()"
			>
				Przejdż do koszyka
			</a>
			<button 
				class="btn btn-block btn__secondary-outline" 
				@click="$modalManager.hide()"
			>
				Kontynuuj zakupy
			</button>
		</div>
	</Modal>
</template>
<script>
import { computed, toRefs } from 'vue'

import Modal from '@/components/Modal';


export default {
	components: {
		Modal
	},
	setup (props) {
		const { context } = toRefs(props)

		const product = computed(() => {
			return context.value.product
		})

		return { product }
	}
}
</script>