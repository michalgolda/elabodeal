// Age category select logic
$( document ).on( 'click', 'div#age-selector', function() {
	var age = Number( $( this ).attr( 'age' ) );
	var age_input = $( 'input[name=age_category]' );

	age_input.attr( 'value', age );
});

// Image upload logic
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
	var inputId = 0;
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
	var parentElement = this.parentElement;
	var parentElementChildren = parentElement.children;

	var fileInput = $( parentElementChildren[ 3 ] );
	var fileName = $( parentElementChildren[ 1 ] );
	var btn = $( this );

	if ( fileInput[ 0 ].files && fileInput[ 0 ].files[ 0 ] ) {
		fileInput[ 0 ].value = '';

		fileName.css( 'display', 'none' );

		btn.removeClass( 'btn__danger' );
		btn.addClass( 'btn__primary' );
		btn.html( 'Prześlij' );
	} else {
		fileInput.trigger( 'click' );
	}
});


$( document ).on( 'change', '#ebook-file-input', function() {
	var parentElement = this.parentElement;
	var parentElementChildren = parentElement.children;

	var fileName = $( parentElementChildren[ 1 ] );
	var uploadBtn = $( parentElementChildren[ 2 ] );

	fileName.html( this.files[ 0 ].name );
	fileName.css( 'display', 'block' );

	uploadBtn.addClass( 'btn__danger' );
	uploadBtn.removeClass( 'btn__primary' );
	uploadBtn.html( 'Usuń' );
});