function getCheckedInput() {
	var inputs = $( $( 'input#age-choice-input' ) );
	for( var i = 0; i < inputs.length; i++ ) {
		if( $( inputs[i] ).attr( 'checked' ) ) {
			return inputs[ i ];
		}
	}

}

$( document ).on( 'click', 'div#age-selector', function() {
	var id = Number( $( this ).attr( 'age-input-id' ) );
	var input = $( $( 'input#age-choice-input' )[ id ] );
	var isChecked = input.attr( 'checked' );

	if( !isChecked ) {
		var checkedInput = getCheckedInput();
		if( checkedInput ) {
			$( checkedInput ).attr( 'checked', false );
			var id = $( checkedInput ).attr('age-input-id');
			var selector = $( $( 'div#age-selector' ) );
			selector.removeClass( 'age-checked' );
		}

		input.attr( 'checked', true );
		$(this).addClass( 'age-checked' );
	} else {
		input.attr( 'checked' , false );
		$(this).removeClass( 'age-checked' );
	}
});

$( document ).on( 'click', 'button#image-upload-btn', function() {
	var inputId = Number( $( this ).attr( 'file-input-id' ) );
	var input = $( $( 'input#image-file-input' )[ inputId ] );

	input.trigger( 'click' );
});

$( document ).on( 'click', 'button#image-delete-btn', function() {
	var id = Number( $( this ).attr( 'file-input-id' ) );
	var imagePreview = $( $( 'div#image-preview' )[ id ] );
	var uploadBtn = $( $( 'button#image-upload-btn' )[ id ] );
	var input = $( $( 'input#image-file-input' )[ id ] );

	input[ 0 ].value = '';

	imagePreview.hide();
	uploadBtn.show()
});

$( document ).on( 'change', 'input#image-file-input', function() {
	var inputId = Number( $( this ).attr( 'name' )[ 11 ] );
	var imagePreview = $( $( 'div#image-preview' )[ inputId ] );
	var previewImg = $( imagePreview ).children( 'img' );
	var uploadBtn = $( $( 'button#image-upload-btn' )[ inputId ] );

	var reader = new FileReader();

	reader.addEventListener( "load", function() {
		previewImg[ 0 ].src = reader.result;

		imagePreview.css('display', 'flex');
		uploadBtn.hide();
	}, false );

	reader.readAsDataURL( $( this )[ 0 ].files[ 0 ]);
});

$( document ).on( 'click', '#ebook-upload-btn', function() {
	var inputId = Number( $( this ).attr( 'file-input-id' ) );
	var input = $( $( 'input#ebook-file-input' )[ inputId ] );
	var fileName = $( $( 'span#file-name' )[ inputId ] );

	var uploadBtn = $( $( 'button#ebook-upload-btn' )[ inputId ] );

	if( input[ 0 ].files && input[ 0 ].files[ 0 ] ) {
		input[ 0 ].value = '';
			
		fileName.css('display', 'none');
		uploadBtn.removeClass( 'btn__danger' );
		uploadBtn.addClass( 'btn__primary' );
		uploadBtn.html( 'Prześlij' );

	} else {
		input.trigger( 'click' );
	}
});

$( document ).on( 'change', '#ebook-file-input', function() {
	var inputName = $( this ).attr( 'name' );
	let inputId = null;

	switch( inputName ) {
		case 'pdf_file':
			inputId = 0;
			break;
		case 'epub_file':
			inputId = 1;
			break;
		case 'mobi_file':
			inputId = 2;
			break;
		case 'demo_pdf_file':
			inputId = 3;
			break;
	}

	var uploadBtn = $( $( 'button#ebook-upload-btn' )[ inputId ] );
	var fileName = $( $( 'span#file-name' )[ inputId ] );
	var uploadProgess = $( $( 'div#file-progress-upload' )[ inputId ] );

	fileName.html( $( this )[ 0 ].files[ 0 ].name );

	fileName.css('display', 'block');
	uploadBtn.addClass( 'btn__danger' );
	uploadBtn.removeClass( 'btn__primary' );
	uploadBtn.html( 'Usuń' );
});