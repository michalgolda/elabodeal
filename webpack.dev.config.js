const path = require( 'path' );
const webpack = require( 'webpack' );

// Plugins
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

// Entrances
const pageEntrances = require('./elabodeal/web/static/js/pages');

const paths = {
	dist: path.resolve(
		__dirname,
		'elabodeal/web/static/dist/'
	),
	globals: path.resolve(
		__dirname,
		'elabodeal/web/static/js/globals/index.js'
	),
	styles: path.resolve(
		__dirname,
		'elabodeal/web/static/styles/main.scss'
	),
	pages: pageEntrances
};

module.exports = {
	mode: 'development',
	devtool: 'cheap-module-eval-source-map',
	entry: {
		...paths.pages,
		globals: paths.globals,
		styles: paths.styles
	},
	output: {
		filename: '[name].bundle.js',
		path: paths.dist
	},
	plugins: [
		new MiniCssExtractPlugin(),
	],
	module: {
		rules: [
			{
				test: /\.(css|sass|scss)$/,
        		use: [
        			MiniCssExtractPlugin.loader, 
        			{
        				loader: 'css-loader',
        				options: {
        					sourceMap: true
        				},
        			},
        			{
        				loader: 'sass-loader',
        				options: {
        					sourceMap: true
        				},
        			}
        		], 
			},
			{
				test: /\.m?js$/,
				exclude: /node_modules/,
				use: {
					loader: "babel-loader"
				}
			}
		],
	},
	optimization: {
		runtimeChunk: {
			name: 'runtime'
		},
		splitChunks: {
			name: 'vendor',
			chunks: 'all'
		}
	},
	watch: true
};
