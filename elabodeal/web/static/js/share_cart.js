var shareCartForm = document.getElementById('share-cart-form');
shareCartForm.addEventListener('submit', function(e) {
    e.preventDefault();
    var formData = new $('#share-cart-form').serializeArray();
    fetch('/api/share/carts/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': window.__csrf_token__
        },
        body: JSON.stringify({
            'title': formData[0]['value'],
            'description': formData[1]['value']
        })
    }).then(response => {
        if (response.ok) {
            const data = response.json().then(data => {
                var clipboard = new ClipboardJS('#share-cart-copy-url');
                var shareCartURLText = document.getElementById('share-cart-url');
                var shareCartForm = $('#share-cart-form');
                var shareCartDetails = $('#share-cart-details');
                var shareCartURLCopyBtn = $('#share-cart-copy-url');
                var sharedCode = data.shared_cart_code;
                var shareURL = `${window.location.origin}/shared/carts/${sharedCode}`;
                shareCartURLText.textContent = shareURL;
                shareCartURLCopyBtn.attr('data-clipboard-text', shareURL);
                clipboard.on('success', function(e) {
                    shareCartURLCopyBtn.html('<i class="fas fa-check"></i>');
                    e.clearSelection();
                });
                shareCartDetails.show();
                shareCartForm.hide();
            })
        } else {
            var displayError = document.getElementById('share-cart-error-msg');
            displayError.textContent = 'Coś poszło nie tak :(';
            Sentry.configureScope(function(scope) {
                scope.setFingerprint('Share-cart-process');
            });
            Sentry.captureException(new Error(response.statusText));
        }
    })
});

function getShareURL() {
    var shareCartURLText = $('#share-cart-url');
    var shareURL = shareCartURLText.html();
    return shareURL;
}
$('#share-fb-btn').click(function() {
    window.open(`https://www.facebook.com/sharer/sharer.php?u=${getShareURL()}`, 'facebook-share', 'width=600, height=500');
});
$('#share-reddit-btn').click(function() {
    window.open(`http://www.reddit.com/submit?url=${getShareURL()}`, 'reddit-share', 'width=600, height=500');
});
$('#share-twitter-btn').click(function() {
    window.open(`https://twitter.com/share?ref_src=${getShareURL()}`, 'twitter-share', 'width=600, height=500');
});
$('#share-email-btn').click(function() {
    window.open(`mailto:?to=&subject=Mój koszyk&body=${getShareURL()}`, 'email-share', 'width=600, height=500');
});