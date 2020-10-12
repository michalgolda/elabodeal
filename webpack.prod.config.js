const path = require( 'path' );
const webpack = require( 'webpack' );

// Plugins
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const CssMinimizerPlugin = require('css-minimizer-webpack-plugin');
const TerserPlugin = require('terser-webpack-plugin');
	

const paths = {
	'dist': path.resolve(
		__dirname, 
		'elabodeal/web/static/dist/'
	),
	'mainEntry': [
		path.resolve(
			__dirname, 
			'elabodeal/web/static/js/index.js'
		),
		path.resolve(
			__dirname,
			'elabodeal/web/static/styles/main.css'
		),
	]
}

module.exports = {
	mode: 'production',
	devtool: 'source-map',
	entry: {
		app: paths.mainEntry
	},
	output: {
		filename: 'main.js',
		path: paths.dist
	},
	plugins: [
		new MiniCssExtractPlugin({
			filename: 'main.css',
		}),
	],
	module: {
		rules: [
			{
				test: /\.css$/i,
        		use: [
        			MiniCssExtractPlugin.loader, 
        			'css-loader'
        		], 
			}
		],
	},
	optimization: {
		minimize: true,
		minimizer: [
			new CssMinimizerPlugin(),
			new TerserPlugin({
				sourceMap: true,
			}),
		],
	},
};