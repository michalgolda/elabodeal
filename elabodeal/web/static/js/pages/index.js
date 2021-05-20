const path = require('path');

module.exports = {
    // publisherSettings: [
    //     path.resolve(
    //         __dirname,
    //         'settings/publisherSettings/index.js'
    //     )
    // ],
    // userSettings: [
    //     path.resolve(
    //         __dirname,
    //         'settings/userSettings/index.js'
    //     )
    // ],
    // productDetails: [
    //     path.resolve(
    //         __dirname,
    //         'productDetails/index.js'
    //     ),
    // ],
    // cart: [
    //     path.resolve(
    //         __dirname,
    //         'cart/index.js'
    //     )
    // ],
    // emailVerification: [
    //     path.resolve(
    //         __dirname,
    //         'emailVerification/index.js'
    //     )
    // ],
    'salesManager~addProductPage': [
        path.resolve(
            __dirname,
            'salesManager/addProduct/index.js'
        )
    ]
}
