const path = require('path');

module.exports = {
    settings: [
        path.resolve(
            __dirname,
            'settings/index.js'
        )
    ],
    userSettings: [
        path.resolve(
            __dirname,
            'settings/userSettings/index.js'
        )
    ],
    productDetails: [
        path.resolve(
            __dirname,
            'productDetails/index.js'
        ),
    ],
    cart: [
        path.resolve(
            __dirname,
            'cart/index.js'
        )
    ],
    emailVerification: [
        path.resolve(
            __dirname,
            'emailVerification/index.js'
        )
    ]
}
