const webpackConfig = require( './webpack.config' );

// Plugins
const CssMinimizerPlugin = require('css-minimizer-webpack-plugin');
const TerserPlugin = require('terser-webpack-plugin');

webpackConfig.mode = 'production';
webpackConfig.devtool = 'source-map';
webpackConfig.optimization = {
	...webpackConfig.optimization,
	minimize: true,
	minimizer: [
		new CssMinimizerPlugin(),
		new TerserPlugin({
			sourceMap: true,
		}),
	]
};
webpackConfig.resolve = {
	alias: {
		'vue': 'vue/dist/vue.min.js'
	}
}

module.exports = webpackConfig;