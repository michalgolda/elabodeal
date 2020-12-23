// ( function( document, window ) {
//     document.addEventListener( 'DOMContentLoaded', function() {
//         var shareCartForm = document.getElementById( 'share-cart-form' );

//         if (!shareCartForm) {
//             return;
//         }

//         shareCartForm.addEventListener( 'submit', function( e ) {
//             e.preventDefault();

//             var formData = new $( '#share-cart-form' ).serializeArray();

//             fetch( '/api/share/carts/', {
//                 method: 'POST',
//                 headers: {
//                     'Content-Type': 'application/json',
//                     'X-CSRFToken': window.__csrf_token__
//                 },
//                 body: JSON.stringify({
//                     'title': formData[0]['value'],
//                     'description': formData[1]['value']
//                 })
//             }).then( res => {
//                 if ( res.ok ) {
//                     const data = res.json().then( data => {
//                         var clipboard = new ClipboardJS( '#share-cart-copy-url' );
                        
//                         var shareCartUrlText = $( '#share-cart-url' );
//                         var shareCartForm = $( '#share-cart-form' );
//                         var shareCartDetails = $( '#share-cart-details' );
//                         var shareCartUrlCopyBtn = $( '#share-cart-copy-url' );
                        
//                         var sharedCode = data.shared_cart_code;
//                         var shareUrl = `${window.location.origin}/shared/carts/${sharedCode}`;

//                         shareCartUrlText.html( shareUrl );             
//                         shareCartUrlCopyBtn.attr( 'data-clipboard-text', shareUrl );
                        
//                         clipboard.on( 'success', function( e ) {
//                             shareCartUrlCopyBtn.html( '<i class="fas fa-check"></i>' );
                            
//                             e.clearSelection();
//                         });
                        
//                         shareCartDetails.show();
//                         shareCartForm.hide();
//                     })
//                 } else {
//                     var statusText = res.statusText;

//                     var errorBox = $( '#share-cart-error-msg' );
//                     errorBox.html( 'Coś poszło nie tak :(' );

//                     Sentry.configureScope( function( scope ) {
//                         scope.setFingerprint( 'Share-cart-process' );
//                     });
//                     Sentry.captureException( new Error( statusText ) );
//                 }
//             })
//         });


//         var shareUrl = $( '#share-cart-url' ).html();

//         $( '#share-fb-btn').click( function() {
//             window.open(
//                 `https://www.facebook.com/sharer/sharer.php?u=${shareUrl}`, 
//                 'facebook-share', 
//                 'width=600, height=500'
//             );
//         });
//         $( '#share-reddit-btn').click( function() {
//             window.open(
//                 `http://www.reddit.com/submit?url=${shareUrl}`, 
//                 'reddit-share', 
//                 'width=600, height=500'
//             );
//         });
//         $( '#share-twitter-btn').click( function() {
//             window.open(
//                 `https://twitter.com/share?ref_src=${shareUrl}`, 
//                 'twitter-share', 
//                 'width=600, height=500'
//             );
//         });
//         $( '#share-email-btn').click( function() {
//             window.open(
//                 `mailto:?to=&subject=Mój koszyk&body=${shareUrl}`, 
//                 'email-share', 
//                 'width=600, height=500'
//             );
//         });

//         $( '#show-save-cart-popup' ).click( function() {
//             $( '#save-cart-popup' ).show();
//         });

//         $( '#close-save-cart-popup' ).click( function() {
//             $( '#save-cart-popup' ).hide();
//         });
//         $( '#open-share-cart-popup').click( function() {
//             $( '#share-cart-popup' ).show();
//         });

//         $( '#close-share-cart-popup' ).click( function() {
//             $( '#share-cart-popup' ).hide();

//             var shareCartUrlCopyBtn = $( '#share-cart-copy-url' );
//             shareCartUrlCopyBtn.html( 'Kopiuj' );
//         });
//     });
// })( document, window );
( function( document, window, jquery, constants ){
    document.addEventListener( 'DOMContentLoaded', function(){
        var popup = document.getElementById( constants.POPUP_ID );

        if( !popup ) return;
        
        var popupShowBtn = document.getElementById( constants.POPUP_SHOW_BTN_ID );
        var popupHideBtn = document.getElementById( constants.POPUP_HIDE_BTN_ID );
        
        popupShowBtn.addEventListener( 'click', function(){
            popup.style.display = 'block';
        });
        
        popupHideBtn.addEventListener( 'click', function(){
            popup.style.display = 'none';
        });
        
        var form = document.getElementById( 'share-cart-form' );
        
        form.addEventListener( 'submit', function( e ){
            e.preventDefault();

            const formData = jquery( this ).serializeArray();
            
            const SHARE_CART_ACTION_URL = window.__actionUrls__['share-cart'];
            const CSRF_TOKEN = window.__csrf_token__;

            jquery.ajax( {
                method: 'POST',
                url: SHARE_CART_ACTION_URL,
                cache: true,
                headers: {
                    'X-CSRFToken': CSRF_TOKEN
                },
                data: formData,
                success: handleSuccess = ( result ) => {
                    const url = result.data['url'];
                    const fullURL = `${window.location.origin}${url}`;

                    var shareDetails = document.getElementById( 'share-details' );
                    
                    var sharedCartUrlElement = document.getElementById( 'shared-cart-url' );
                    sharedCartUrlElement.value = fullURL;

                    this.style.display = 'none';
                    shareDetails.style.display = 'block';

                    var clipboard = new ClipboardJS( '#copy-shared-cart-url' );
                    var sharedCartUrlCopyBtn = document.getElementById( 'copy-shared-cart-url' );
                    
                    sharedCartUrlCopyBtn.setAttribute( 'data-clipboard-text', fullURL );
                    
                    clipboard.on( 'success', function( e ) {
                       sharedCartUrlCopyBtn.textContent = 'Skopiowano';

                       setTimeout(function(){
                        sharedCartUrlCopyBtn.textContent = 'Kopiuj';
                       }, 2000);

                        e.clearSelection();
                    });
                },
                error: handleError = ( error ) => {
                    console.error(error);
                }
            } );
            
        });
    });
})( document, window, $, {
    'POPUP_ID': 'share-cart-popup',
    'POPUP_SHOW_BTN_ID': 'show-share-cart-popup',
    'POPUP_HIDE_BTN_ID': 'hide-share-cart-popup'
});