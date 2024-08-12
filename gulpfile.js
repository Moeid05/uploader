var gulp = require('gulp');
const npmDist = require('gulp-npm-dist');
var rename = require("gulp-rename");

const paths = {
    src: {
        base: './static/assets',
        css: './static/assets/css',
    }
};

gulp.task('css', function() {
    return gulp.src([
            paths.src.css + '/black-dashboard.css'
        ])
        .pipe(cleanCss())
        .pipe(rename(function(path) {
            // Updates the object in-place
            path.extname = ".min.css";
        }))
        .pipe(gulp.dest(paths.src.css))
});

// Minify CSS
gulp.task('minify:css', function() {
    return gulp.src([
            paths.src.css + '/black-dashboard.css'
        ])
        .pipe(cleanCss())
        .pipe(rename(function(path) {
            // Updates the object in-place
            path.extname = ".min.css";
        }))
        .pipe(gulp.dest(paths.src.css))
});

// Default Task: Compile SCSS and minify the result
gulp.task('default', gulp.series('scss', 'minify:css'));
