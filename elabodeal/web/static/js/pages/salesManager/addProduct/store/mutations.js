const mutations = {
	updateFormData: function ( state, payload ) {
		const { fieldName, fieldValue } = payload;

		state.formData[ fieldName ] = fieldValue;
	}
}

export default mutations;