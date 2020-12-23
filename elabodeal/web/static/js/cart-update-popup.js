( function( document, window, constants ) {
	document.addEventListener( 'DOMContentLoaded', function() {
		var popup = document.getElementById( constants.POPUP_ID );

		if ( !popup ) return;

		var popupCloseBtn = document.getElementById( constants.POPUP_CLOSE_BTN_ID );

		popup.style.display = 'block';

		var popupActions = $( '*#popup-action' );

		var popupContinueShoppingBtn = popupActions[0];

		popupContinueShoppingBtn.addEventListener( 'click', function() {
			popup.style.display = 'none';
		});

		popupCloseBtn.addEventListener( 'click', function() {
			popup.style.display = 'none';
		});
	});
})( document, window, {
	'POPUP_ID': 'cart-update-popup',
	'POPUP_CLOSE_BTN_ID': 'close-cart-update-popup'
} );