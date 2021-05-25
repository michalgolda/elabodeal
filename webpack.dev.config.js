const webpackConfig = require( './webpack.config' );

webpackConfig.mode = 'development';
webpackConfig.devtool = 'eval';
webpackConfig.watch = true;
webpackConfig.resolve = {
    alias: {
        'vue': '@vue/runtime-dom'
    }
}

module.exports = webpackConfig;