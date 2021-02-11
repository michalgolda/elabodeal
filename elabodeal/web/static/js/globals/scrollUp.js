$( '#js-scrollup-btn' ).on( 'click', () => {
    $( 'html, body' ).animate( {
        scrollTop: 0
    }, 1000 );
} );