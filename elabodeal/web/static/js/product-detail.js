$( '#show-product-contents-btn' ).click( function() {
	$( this ).removeClass( 'btn__primary-outline' );
	$( this ).addClass( 'btn__primary' );

	var showDescriptionBtn = $( '#show-product-description-btn' );

	showDescriptionBtn.removeClass( 'btn__primary' );
	showDescriptionBtn.addClass( 'btn__primary-outline' );
	
	$( '#product-description' ).hide();
	$( '#product-contents' ).show();
});

$( '#show-product-description-btn' ).click( function() {
	$( this ).removeClass( 'btn__primary-outline' );
	$( this ).addClass( 'btn__primary' );

	var showContentsBtn = $( '#show-product-contents-btn' );

	showContentsBtn.removeClass( 'btn__primary' );
	showContentsBtn.addClass( 'btn__primary-outline' );
	
	$( '#product-description' ).show();
	$( '#product-contents' ).hide();
});