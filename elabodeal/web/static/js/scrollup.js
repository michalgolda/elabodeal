( function( document, window ){
	document.addEventListener( 'DOMContentLoaded', function(){
		var scrollUpBtn = document.getElementById( 'scrollUpBtn' );

		if (!scrollUpBtn) return;

		scrollUpBtn.addEventListener( 'click', function(){
			$( 'html, body' ).animate({
				scrollTop: 0
			}, 1000);
		});
	});
})( document, window );