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
			@click="removeProductFromCart"
		>
			<i class="fas fa-times h2 product__delete" />
		</button>
	</div>
</template>
<script>
import { useStore } from 'vuex'
import { mainModuleTypes } from '../store/modules';


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
		const { productId } = props

		const store = useStore()

		const toggleProduct = (e) => {
			const selected = e.target.checked

			store.dispatch(
				mainModuleTypes.actions.TOGGLE_PRODUCT,
				{ productId, selected }
			)
		}

		const removeProductFromCart = () => {
			store.dispatch(
				mainModuleTypes.actions.REMOVE_PRODUCT_FROM_CART,
				{ productId }
			)
		}

		return {
			toggleProduct,
			removeProductFromCart
		}
	}
}
</script>