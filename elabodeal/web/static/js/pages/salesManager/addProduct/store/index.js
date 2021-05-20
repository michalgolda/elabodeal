import { createStore } from "vuex";
import mutations from "./mutations";


const store = createStore( {
	state: function () {
		const { 
			fee,
			categories, 
			supportedLanguages 
		} = window.__APP_CONTEXT__.data;

		return {
			fee,
			categories,
			supportedLanguages,
			form: {
				isValid: false,
				fields: {
					category_id: {
						value: null,
						required: true,
						error: false
					},
					product_language_id: {
						value: null,
						required: true,
						error: false
					},
					age_category: {
						value: 3,
						required: true,
						error: false
					},
					page_count: {
						value: null,
						required: true,
						error: false
					},
					published_year: {
						value: null,
						required: true,
						error: false
					},
					title: {
						value: null,
						required: true,
						error: false
					},
					author: {
						value: null,
						required: true,
						error: false
					},
					price: {
						value: null,
						required: true,
						error: false
					},
					copies: {
						value: 0,
						required: false,
						error: false
					},
					description: {
						value: null,
						required: true,
						error: false
					},
					contents: {
						value: null,
						required: false,
						error: false
					},
					isbn: {
						value: null,
						required: true,
						error: false
					},
					cover_img: {
						value: null,
						required: true,
						error: false
					},
					files: {
						value: [],
						required: true,
						error: false
					},
					other_images: {
						value: [],
						required: false,
						error: false
					},
					premiere_datetime: {
						value: null,
						required: false,
						error: false
					}
				}
			}
		}
	},
	mutations: mutations
} )

export default store;