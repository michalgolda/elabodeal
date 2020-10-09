$( '#show-contents-btn' ).click( function() {
	$( this ).removeClass( 'btn-outline-orange' );
	$( this ).addClass( 'btn-orange' );

	var showDescriptionBtn = $( '#show-description-btn' );

	showDescriptionBtn.removeClass( 'btn-orange' );
	showDescriptionBtn.addClass( 'btn-outline-orange' );
	
	$( '#product-description' ).hide();
	$( '#product-contents' ).show();
});

$( '#show-description-btn' ).click( function() {
	$( this ).removeClass( 'btn-outline-orange' );
	$( this ).addClass( 'btn-orange' );

	var showContentsBtn = $( '#show-contents-btn' );

	showContentsBtn.removeClass( 'btn-orange' );
	showContentsBtn.addClass( 'btn-outline-orange' );
	
	$( '#product-description' ).show();
	$( '#product-contents' ).hide();
});