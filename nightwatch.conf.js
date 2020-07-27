module.exports = {
  src_folders: ['tests'],

  webdriver: {
    start_process: true,
    port: 4444,
    server_path: require('geckodriver').path,
    cli_args: [
      '-vv'
    ]
  },

  test_settings: {
    default: {
      launch_url: 'http://localhost:8000',
      desiredCapabilities : {
        browserName : 'firefox',
        alwaysMatch: {
          // Enable this if you encounter unexpected SSL certificate errors in Firefox
          // acceptInsecureCerts: true,
          'moz:firefoxOptions': {
            args: [
              '-headless',
              '-verbose'
            ],
          }
        }
      }
    }
  }
};
