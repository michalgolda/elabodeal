if( $( '#show-gift-form' ).attr( 'checked' ) ) {
	$( '#gift-form' ).show();
}

$( '#show-gift-form' ).click( function() {
	if( $( '#gift-form' ).is( ':hidden' ) ){
        $( '#gift-form' ).show();
    } else {
        $( '#gift-form' ).hide();
    }
});