<template>
	<div class="product">
		<div class="flex-center">
			<input 
				type="checkbox" 
				checked
				@change="handleToggleProduct"
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
			@click="handleRemoveProduct"
		>
			<i class="fas fa-times h2 product__delete" />
		</button>
	</div>
</template>
<script>
import { mapActions, mapMutations } from 'vuex';


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
		}
	},
	methods: {
		...mapActions(['removeProductFromCart']),
		...mapMutations(['selectProduct', 'unSelectProduct']),
		handleRemoveProduct () {
			this.removeProductFromCart({
				product_id: this.productId
			});
		},
		handleToggleProduct (e) {
			const { checked } = e.target;

			const actionType = checked ? 'SELECT' : 'UNSELECT';

			switch (actionType) {
				case 'SELECT':
					this.selectProduct(this.productId);

					break;
				case 'UNSELECT':
					this.unSelectProduct(this.productId);

					break;
			}
		}
	}
}
</script>