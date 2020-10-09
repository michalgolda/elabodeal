const path = require( 'path' );
const webpack = require( 'webpack' );

console.log(__dirname);

const paths = {
	'appBuild': path.resolve(
		__dirname, 
		'elabodeal/web/static/js/dist/'
	),
	'appEntry': path.resolve(
		__dirname, 
		'elabodeal/web/static/js/index.js'
	)	
}

module.exports = {
	mode: 'development',
	entry: {
		app: paths.appEntry
	},
	output: {
		filename: 'app.js',
		path: paths.appBuild
	},
	watch: true
}