const webpackConfig = require( './webpack.config' );

const FriendlyErrorsWebpackPlugin = require('friendly-errors-webpack-plugin');


webpackConfig.mode = 'development';
webpackConfig.devtool = 'eval';
webpackConfig.watch = true;
webpackConfig.watchOptions = {
	ignored: ['/node_modules/']
};

webpackConfig.plugins.push(new FriendlyErrorsWebpackPlugin());

module.exports = webpackConfig;