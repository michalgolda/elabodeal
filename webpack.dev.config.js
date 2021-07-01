const webpackConfig = require( './webpack.config' );

const FriendlyErrorsWebpackPlugin = require('friendly-errors-webpack-plugin');


webpackConfig.mode = 'development';
webpackConfig.devtool = 'eval';

webpackConfig.module.rules.push({
	enforce: 'pre',
	test: /\.(js|vue)$/,
	exclude: /node_modules/,
	loader: 'eslint-loader',
	options: {
		formatter: 'codeframe'
	}
});

webpackConfig.watch = true;
webpackConfig.watchOptions = {
	ignored: ['/node_modules/']
};

webpackConfig.plugins.push(new FriendlyErrorsWebpackPlugin());

module.exports = webpackConfig;