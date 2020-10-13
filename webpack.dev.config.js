const path = require( 'path' );
const webpack = require( 'webpack' );

// Plugins
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
	

const paths = {
	'dist': path.resolve(
		__dirname, 
		'elabodeal/web/static/dist/'
	),
	'mainEntrances': [
		path.resolve(
			__dirname, 
			'elabodeal/web/static/js/index.js'
		),
		path.resolve(
			__dirname,
			'elabodeal/web/static/styles/main.scss'
		),
	]
}

module.exports = {
	mode: 'development',
	devtool: 'cheap-module-eval-source-map',
	entry: {
		app: paths.mainEntrances
	},
	output: {
		filename: 'app.js',
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
			}
		],
	},
	watch: true
};
