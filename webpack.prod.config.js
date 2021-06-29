const webpackConfig = require( './webpack.config' );

// Plugins
const TerserPlugin = require('terser-webpack-plugin');
const CssMinimizerPlugin = require('css-minimizer-webpack-plugin');


webpackConfig.mode = 'production';
webpackConfig.optimization = {
	...webpackConfig.optimization,
	minimize: true,
	minimizer: [
		new CssMinimizerPlugin(),
		new TerserPlugin(),
	]
};

module.exports = webpackConfig;