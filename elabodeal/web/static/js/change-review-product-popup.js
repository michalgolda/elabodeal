var popup = $( '#change-review-product-popup' );
var popupOpenBtn = $( '#open-change-review-product-popup' );
var popupCloseBtn = $( '#close-change-review-product-popup' );

popupOpenBtn.click( function() {
	popup.show();
});

popupCloseBtn.click( function() {
	popup.hide();
});

function reverseRatingNumber( number ) {
	switch( number ) {
		case 5:
			return 1
		case 4:
			return 2;
		case 3:
			return 3;
		case 2:
			return 4;
		case 1:
			return 5;
	}
}

$( document ).on( 'click', 'i#star', function() {
	var rating = reverseRatingNumber( Number( $( this ).attr( 'star' ) ) );
	var ratingInput = $( '#rating-input' );
	
	ratingInput.attr( 'value', rating );
});