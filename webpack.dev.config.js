const webpackConfig = require( './webpack.config' );

webpackConfig.mode = 'development';
webpackConfig.devtool = 'cheap-module-eval-source-map';
webpackConfig.watch = true;
webpackConfig.resolve = {
    alias: {
        'vue': 'vue/dist/vue.js'
    }
}

module.exports = webpackConfig;