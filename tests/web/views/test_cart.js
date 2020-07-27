describe('Tests for cart page', function() {
	test('Test cart page', function(browser) {
		browser
	    	.url(`${browser.options.launch_url}/cart/`)
	      	.waitForElementVisible('body')
	      	.assert.title('Elabodeal - Twój koszyk')
	     	.assert.elementPresent('.nav')
	      	.assert.elementPresent('.footer')
	      	.assert.elementPresent('button[type=share]')
		    .assert.containsText('button[type=share]', 'Udostępnij koszyk')
	     	.end();
	})
})