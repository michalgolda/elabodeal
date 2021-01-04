( function( document ){
	document.addEventListener( 'DOMContentLoaded', function(){
		var scrollUpBtn = document.getElementById( 'js-scrollup-btn' );

		if ( !scrollUpBtn ) return;

		scrollUpBtn.addEventListener( 'click', function(){
			$( 'html, body' ).animate({
				scrollTop: 0
			}, 1000);
		} );
	} );
} )( document );