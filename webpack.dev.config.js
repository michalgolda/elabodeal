const webpackConfig = require( './webpack.config' );

webpackConfig.mode = 'development';
webpackConfig.devtool = 'eval';
webpackConfig.watch = true;

module.exports = webpackConfig;