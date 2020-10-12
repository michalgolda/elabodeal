const openEditBoxButtons = $( 'button#open-edit-box-btn' );

let editMode = false;

$( openEditBoxButtons ).click( function( e ) {
	if( !editMode ) {
		const currTarget = $( e.target );

		/* Hide btn which open edit box */
		currTarget.hide();

		const editBoxIndex = parseInt( currTarget.attr( 'edit-box-index' ) );
		const editBox = $( $( '.edit-box' )[ editBoxIndex ] );

		const changeInputId = editBox.attr( 'change-input-id' );
		const valueElemId = editBox.attr( 'value-elem-id' );
		const submitBtnIndex = parseInt( editBox.attr( 'submit-change-btn-index' ) );
		const cancelBtnIndex = parseInt( editBox.attr( 'cancel-change-btn-index' ) );
		const dataFieldName = editBox.attr( 'data-field-name' );

		const changeInput = $( `#${changeInputId}` );
		const valueElem = $( `#${valueElemId}` );
		const submitBtn = $( $( `button#submit-change-btn` )[ submitBtnIndex ] );
		const cancelBtn = $( $( 'button#cancel-change-btn' )[ cancelBtnIndex ] );

		// Helper functions
		const openEditMode = () => {
			changeInput.show();
			submitBtn.show();
			cancelBtn.show();

			valueElem.hide();

			/* When someone open the edit box copy value from valueElem to changeInput,
			  set that value to default value on input
			*/
			const defaultValue = valueElem.html();
			changeInput.val( defaultValue );

			editMode = true;
		};

		const exitEditMode = () => {
			submitBtn.hide();
			cancelBtn.hide();
			changeInput.hide();

			currTarget.show();
			valueElem.show();

			editMode = false;
		};

		// When someone click on open edit box btn this function is execute
		openEditMode();


		// Submit change to server
		submitBtn.click(function(e) {
			changeInputValue = changeInput.val();

			bodyData = fieldsForUpdate;
			bodyData[ `${dataFieldName}` ] = changeInputValue;

			fetch( `/api/product/${currentProductId}/`, {
				method: 'PUT',
				headers: {
					'Content-Type': 'application/json',
					'X-CSRFToken': window.__csrf_token__
				},
				body: JSON.stringify(bodyData)
			})
			.then( response => {
				if( response.ok ) {
					exitEditMode();

					// Update valueElem with new value
					valueElem.html( changeInputValue );
				} else {
					exitEditMode();

					Sentry.configureScope( function( scope ) {
					  scope.setFingerprint( 'Product-update-proccess' );
					  scope.setTag( 'update-field-name', dataFieldName );
					});
					Sentry.captureException( new Error( response.statusText ) );
				}
			})
		});

		cancelBtn.click( function( e ) {
			exitEditMode();
		});
	} 
});