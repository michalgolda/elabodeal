var popup = $( '#add-product-to-cart-info-popup' );
var popupCloseBtn = $( '#close-add-product-to-cart-info-popup' );
var popupContinueShopping = $( '#continue-shopping' );

popup.removeClass( 'display-none' );

popupCloseBtn.click( function() {
	popup.hide();
});

popupContinueShopping.click( function() {
	popup.hide();
});