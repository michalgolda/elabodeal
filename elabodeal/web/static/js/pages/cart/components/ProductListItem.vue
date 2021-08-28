<template>
	<div class="product">
		<div class="flex-center">
			<input 
				type="checkbox" 
				:checked="selected"
				@change="toggleProduct"
			>
		</div>
		<img 
			:src="coverImgPath" 
			style="width:100%;" 
		>
		<div class="product__details">
			<div>
				<h3 class="product__title">
					{{ title }}
				</h3>
				<p class="product__author">
					{{ author }}
				</p>
			</div>
			<div>
				<p class="product__price">
					{{ price }} zł
				</p>
			</div>
		</div>
		<button 
			style="background-color: transparent; border: none; outline: none;"
			@click="removeProduct"
		>
			<i class="fas fa-times h2 product__delete" />
		</button>
	</div>
</template>
<script>
import { toRefs } from 'vue'
import { useStore } from 'vuex'

import { actionsTypes } from '../store/actions'


export default {
	props: {
		title: {
			type: String,
			required: true
		},
		author: {
			type: String,
			required: true
		},
		price: {
			type: Number,
			required: true
		},
		coverImgPath: {
			type: String,
			required: true
		},
		productId: {
			type: String,
			required: true
		},
		selected: {
			type: Boolean,
			required: true
		}
	},
	setup (props) {
		const { productId } = toRefs(props)

		const store = useStore()

		const toggleProduct = (e) => {
			const actionType = e.target.checked ? 'DESELECT' : 'SELECT'

			switch (actionType) {
				case 'SELECT':
					store.dispatch(
						actionsTypes.SELECT_PRODUCT, 
						{ productId: productId.value }
					)

					break
				case 'DESELECT':
					store.dispatch(
						actionsTypes.DESELECT_PRODUCT,
						{ productId: productId.value }
					)

					break
			}
		}

		const removeProduct = () => {
			store.dispatch(
				actionsTypes.REMOVE_PRODUCT,
				{ productId: productId.value }
			)
		}

		return {
			toggleProduct,
			removeProduct
		}
	}
}
</script>