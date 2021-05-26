const path = require( 'path' );
const webpack = require( 'webpack' );

// Plugins
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const VueLoader = require('vue-loader');
const RemoveEmptyScriptsPlugin = require("webpack-remove-empty-scripts");

const entry = require("./webpack.entry");

module.exports = {
	entry: entry,
	output: {
		filename: '[name].js',
		path: path.resolve(
			__dirname,
			"elabodeal/web/static/dist/"
		)
	},
	plugins: [
		new RemoveEmptyScriptsPlugin(),
		new MiniCssExtractPlugin(),
		new VueLoader.VueLoaderPlugin(),
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
			},
			{
				test: /\.vue$/,
				loader: 'vue-loader'
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
	}
};