// Karma configuration
// Generated on Mon Sep 22 2014 22:07:17 GMT-0700 (PDT)

module.exports = function(config) {
  config.set({

    // base path that will be used to resolve all patterns (eg. files, exclude)
    basePath: '',


    // frameworks to use
    // available frameworks: https://npmjs.org/browse/keyword/karma-adapter
    frameworks: ['jasmine'],


    // list of files / patterns to load in the browser
    files: [
      '../js/jquery-1.10.2.min.js',
      '../js/jquery-ui.min.js',
      '../js/jquery.geocomplete.min.js',
      '../js/jquery.address.js',
      '../js/bootstrap.min.js',
      '../js/underscore-min.js',
      '../js/backbone-min.js',
      '../js/autocomplete.js',
      '../js/html5.js',
      '../js/places.js',
      '../js/maps_lib.js',
      '../js/collections/*.js',
      '../js/lib/*.js',
      '../js/models/*.js',
      '../js/views/*.js',
//      '../js/app.js',
      '*.test.js',
      '*.js'
    ],


    // list of files to exclude
    exclude: [
    ],


    // preprocess matching files before serving them to the browser
    // available preprocessors: https://npmjs.org/browse/keyword/karma-preprocessor
    preprocessors: {
    },


    // test results reporter to use
    // possible values: 'dots', 'progress'
    // available reporters: https://npmjs.org/browse/keyword/karma-reporter
    reporters: ['progress'],


    // web server port
    port: 9876,


    // enable / disable colors in the output (reporters and logs)
    colors: true,


    // level of logging
    // possible values: config.LOG_DISABLE || config.LOG_ERROR || config.LOG_WARN || config.LOG_INFO || config.LOG_DEBUG
    logLevel: config.LOG_INFO,


    // enable / disable watching file and executing tests whenever any file changes
    autoWatch: true,


    // start these browsers
    // available browser launchers: https://npmjs.org/browse/keyword/karma-launcher
    browsers: ['Chrome'],


    // Continuous Integration mode
    // if true, Karma captures browsers, runs the tests and exits
    singleRun: false
  });
};
