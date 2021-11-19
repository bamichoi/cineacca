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
    .pipe(gulp.dest("backend/static/css")); 
};

const email = () => {
  const postCSS = require("gulp-postcss");
  const sass = require("gulp-sass")(require("node-sass"));
  const minify = require("gulp-csso");
  return gulp
    .src("assets/scss/email/verify_email.scss")
    .pipe(sass().on("error", sass.logError))
    .pipe(postCSS([require("autoprefixer")]))
    .pipe(minify())
    .pipe(gulp.dest("static/email/css")); 
}

const watch = () => {
  gulp.watch(["assets/scss/*", "assets/scss/*/*", "assets/scss/*/*/*" ], css)
}


exports.default = gulp.series(css, email, watch);