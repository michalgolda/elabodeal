const mutations = {
	updateFormData: function ( state, payload ) {
		const { fieldName, fieldValue } = payload;
		const field = state.form.fields[ fieldName ];

		if ( field.error ) field.error = false;

		field.value = fieldValue;
	},
	validateFormData: function ( state ) {
		const fieldNames = Object.keys( state.form.fields );

		var isValid = true;

		for ( var fieldName of fieldNames ) {
			const field = state.form.fields[ fieldName ];

			if ( field.required ) {
				if ( field.value instanceof Array ) {
					if ( field.value.length === 0 ) {
						field.error = true;
						isValid = false;
					}
				} else {
					if ( field.value === null ) {
						field.error = true;
						isValid = true;
					}
				}
			}
		}

		state.form.isValid = isValid;
	},
	clearFieldError: function ( state, payload ) {
		const { fieldName } = payload;
		const field = state.form.fields[ fieldName ];

		field.error = false;
	}
}

export default mutations;