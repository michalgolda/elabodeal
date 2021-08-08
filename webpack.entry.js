const path = require("path");


const STATIC_PATH = path.resolve(__dirname, "elabodeal/web/static/");

module.exports = {
	"userRegisterConfirmationPage": [
		path.resolve(STATIC_PATH, "js/pages/userRegisterConfirmation/index.js"),
		path.resolve(STATIC_PATH, "styles/pages/user-register-confirmation.scss")
	],
	"sharedCartPage": [
		path.resolve(STATIC_PATH, "styles/pages/shared-cart.scss")
	],
	"savedCartDetailsPage": [
		path.resolve(STATIC_PATH, "js/pages/savedCartDetails/index.js"),
		path.resolve(STATIC_PATH, "styles/pages/saved-cart-details.scss")
	],
	"cartCheckoutPage": [
		path.resolve(STATIC_PATH, "js/pages/cartCheckout/index.js"),
		path.resolve(STATIC_PATH, "styles/pages/cart-checkout.scss")
	],
	"productPage": [
		path.resolve(STATIC_PATH, "js/pages/product/index.js"),
		path.resolve(STATIC_PATH, "styles/pages/product.scss")
	],
	"indexPage": [
		path.resolve(STATIC_PATH, "styles/pages/index.scss")
	],
	"authPage": [
		path.resolve(STATIC_PATH, "styles/pages/auth.scss")
	],
	"settingsPage": [
		path.resolve(STATIC_PATH, "js/pages/settings/index.js"),
		path.resolve(STATIC_PATH, "styles/pages/settings.scss")
	],
	"cartPage": [
		path.resolve(STATIC_PATH, "js/pages/cart/index.js"),
		path.resolve(STATIC_PATH, "styles/pages/cart.scss")
	],
	"salesManager~indexPage": [
		path.resolve(STATIC_PATH, "styles/pages/salesManager/index.scss")
	],
	"salesManager~startPage": [
		path.resolve(STATIC_PATH, "js/pages/salesManager/start/index.js"),
		path.resolve(STATIC_PATH, "styles/pages/salesManager/start.scss")
	],
	"salesManager~addProductPage": [
		path.resolve(STATIC_PATH, "js/pages/salesManager/addProduct/index.js"),
		path.resolve(STATIC_PATH, "styles/pages/salesManager/add-product.scss")
	],
	globals: [
		path.resolve(STATIC_PATH, "styles/globals.scss"),
		path.resolve(STATIC_PATH, "js/globals/index.js")
	]
}