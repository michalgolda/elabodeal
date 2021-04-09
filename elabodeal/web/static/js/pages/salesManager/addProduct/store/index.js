import { createStore } from "vuex";
import mutations from "./mutations";


const store = createStore( {
	state: function () {
		const { categories, supportedLanguages } = window.__APP_CONTEXT__.data;

		return {
			categories,
			supportedLanguages,
			formData: {
				category_id: '',
				age_category: 3,
				product_language_id: '',
				page_count: null,
				published_year: null,
				title: '',
				author: '',
				price: 0.00,
				description: '',
				contents: '',
				isbn: '',
				files: [],
				other_images: [],
				cover_img: null
			}
		}
	},
	mutations: mutations
} )

export default store;