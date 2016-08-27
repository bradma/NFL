'use strict';

var gulp = require("gulp"),
    mainBowerFiles = require('main-bower-files'),
    $ = require('gulp-load-plugins')();

gulp.task('bower-scripts', function() {
    var filter = $.filter('*.js');
    return gulp.src(mainBowerFiles({
        filter: '**/*.js'
    }), { base: 'static_dev/bower_components' })
        .pipe($.concat('vendor.js'))
        .pipe($.uglify())
        .pipe($.rename('vendor.min.js'))
        .pipe(gulp.dest('static/javascripts'))
});
