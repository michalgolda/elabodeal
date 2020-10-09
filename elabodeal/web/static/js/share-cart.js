( function( document, window ) {
    document.addEventListener( 'DOMContentLoaded', function() {
        var shareCartForm = document.getElementById( 'share-cart-form' );

        if (!shareCartForm) {
            return;
        }

        shareCartForm.addEventListener( 'submit', function( e ) {
            e.preventDefault();

            var formData = new $( '#share-cart-form' ).serializeArray();

            fetch( '/api/share/carts/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': window.__csrf_token__
                },
                body: JSON.stringify({
                    'title': formData[0]['value'],
                    'description': formData[1]['value']
                })
            }).then( res => {
                if ( res.ok ) {
                    const data = res.json().then( data => {
                        var clipboard = new ClipboardJS( '#share-cart-copy-url' );
                        
                        var shareCartUrlText = $( '#share-cart-url' );
                        var shareCartForm = $( '#share-cart-form' );
                        var shareCartDetails = $( '#share-cart-details' );
                        var shareCartUrlCopyBtn = $( '#share-cart-copy-url' );
                        
                        var sharedCode = data.shared_cart_code;
                        var shareUrl = `${window.location.origin}/shared/carts/${sharedCode}`;

                        shareCartUrlText.html( shareUrl );             
                        shareCartUrlCopyBtn.attr( 'data-clipboard-text', shareUrl );
                        
                        clipboard.on( 'success', function( e ) {
                            shareCartUrlCopyBtn.html( '<i class="fas fa-check"></i>' );
                            
                            e.clearSelection();
                        });
                        
                        shareCartDetails.show();
                        shareCartForm.hide();
                    })
                } else {
                    var statusText = res.statusText;

                    var errorBox = $( '#share-cart-error-msg' );
                    errorBox.html( 'Coś poszło nie tak :(' );

                    Sentry.configureScope( function( scope ) {
                        scope.setFingerprint( 'Share-cart-process' );
                    });
                    Sentry.captureException( new Error( statusText ) );
                }
            })
        });


        var shareUrl = $( '#share-cart-url' ).html();

        $( '#share-fb-btn').click( function() {
            window.open(
                `https://www.facebook.com/sharer/sharer.php?u=${shareUrl}`, 
                'facebook-share', 
                'width=600, height=500'
            );
        });
        $( '#share-reddit-btn').click( function() {
            window.open(
                `http://www.reddit.com/submit?url=${shareUrl}`, 
                'reddit-share', 
                'width=600, height=500'
            );
        });
        $( '#share-twitter-btn').click( function() {
            window.open(
                `https://twitter.com/share?ref_src=${shareUrl}`, 
                'twitter-share', 
                'width=600, height=500'
            );
        });
        $( '#share-email-btn').click( function() {
            window.open(
                `mailto:?to=&subject=Mój koszyk&body=${shareUrl}`, 
                'email-share', 
                'width=600, height=500'
            );
        });

        $( '#show-save-cart-popup' ).click( function() {
            $( '#save-cart-popup' ).show();
        });

        $( '#close-save-cart-popup' ).click( function() {
            $( '#save-cart-popup' ).hide();
        });
        $( '#open-share-cart-popup').click( function() {
            $( '#share-cart-popup' ).show();
        });

        $( '#close-share-cart-popup' ).click( function() {
            $( '#share-cart-popup' ).hide();

            var shareCartUrlCopyBtn = $( '#share-cart-copy-url' );
            shareCartUrlCopyBtn.html( 'Kopiuj' );
        });
    });
})( document, window );
