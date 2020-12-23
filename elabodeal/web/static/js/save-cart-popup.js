// import { alert } from './alert';

( function( document, window, jquery, constants ){
    document.addEventListener( 'DOMContentLoaded', function(){
        var popup = document.getElementById( constants.POPUP_ID );

        if ( !popup ) return;

        var popupShowBtn = document.getElementById( constants.POPUP_SHOW_BTN_ID );
        var popupHideBtn = document.getElementById( constants.POPUP_HIDE_BTN_ID );

        popupShowBtn.addEventListener( 'click', function(){
            popup.style.display = 'block';
        } );

        popupHideBtn.addEventListener( 'click', function(){
            popup.style.display = 'none';
        } );

        var form = document.getElementById( 'save-cart-form' );

        form.addEventListener( 'submit', function( e ){
            e.preventDefault();

            const formData = jquery( this ).serializeArray();

            const SAVE_CART_ACTION_URL = window.__actionUrls__['save-cart'];
            const CSRF_TOKEN = window.__csrf_token__;

            jquery.ajax( {
                url: SAVE_CART_ACTION_URL,
                method: 'POST',
                headers: {
                    'X-CSRFToken': CSRF_TOKEN
                },
                data: formData,
                success: ( result ) => {
                    popup.style.display = 'none';
                },
                error: ( error ) => {
                    popup.style.display = 'none';
                }
            } );
        } );
    } );
} )( document, window, $, {
    'POPUP_ID': 'save-cart-popup',
    'POPUP_SHOW_BTN_ID': 'show-save-cart-popup',
    'POPUP_HIDE_BTN_ID': 'hide-save-cart-popup'
} );