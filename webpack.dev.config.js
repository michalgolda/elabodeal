const webpackConfig = require( './webpack.config' );

const FriendlyErrorsWebpackPlugin = require('friendly-errors-webpack-plugin');


webpackConfig.mode = 'development';
webpackConfig.devtool = 'eval';
webpackConfig.watch = true;
webpackConfig.plugins = [
	...webpackConfig.plugins,
	new FriendlyErrorsWebpackPlugin()
];

module.exports = webpackConfig;