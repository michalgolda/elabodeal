const path = require("path");


const STATIC_PATH = path.resolve(__dirname, "elabodeal/web/static/");

module.exports = {
	"indexPage": [
		path.resolve(STATIC_PATH, "styles/pages/index.scss")
	],
	"authPage": [
		path.resolve(STATIC_PATH, "styles/pages/auth.scss")
	],
	"cart~indexPage": [
		path.resolve(STATIC_PATH, "styles/pages/cart/index.scss")
	],
	"cart~deliveryPage": [
		path.resolve(STATIC_PATH, "styles/pages/cart/delivery.scss")
	],
	"cart~paymentPage": [
		path.resolve(STATIC_PATH, "styles/pages/cart/payment.scss")
	],
	"cart~paymentSuccessPage": [
		path.resolve(STATIC_PATH, "styles/pages/cart/payment-success.scss")
	],
	"salesManager~addProductPage": [
		path.resolve(STATIC_PATH, "js/pages/salesManager/addProduct/index.js"),
		path.resolve(STATIC_PATH, "styles/pages/salesManager/add-product.scss")
	],
	"salesManager~startPage": [
		path.resolve(STATIC_PATH, "styles/pages/salesManager/start.scss")
	],
	globals: [
		path.resolve(STATIC_PATH, "styles/globals.scss"),
		path.resolve(STATIC_PATH, "js/globals/index.js")
	]
}