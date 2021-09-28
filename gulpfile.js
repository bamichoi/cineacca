const gulp = require("gulp");

const css = () => {
  const postCSS = require("gulp-postcss");
  const sass = require("gulp-sass")(require("node-sass"));
  const minify = require("gulp-csso");
  return gulp
    .src("assets/scss/styles.scss")
    .pipe(sass().on("error", sass.logError))
    .pipe(postCSS([require("autoprefixer")]))
    .pipe(minify())
    .pipe(gulp.dest("static/css"));
};

exports.default = css;