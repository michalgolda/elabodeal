var popup = $( '#review-product-popup' );
var popupOpenBtn = $( '#open-review-product-popup' );
var popupCloseBtn = $( '#close-review-product-popup' );

popupOpenBtn.click(function(){
	popup.show();
});

popupCloseBtn.click(function() {
	popup.hide();
});