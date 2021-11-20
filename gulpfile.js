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

const js = () => {
  const bro = require("gulp-bro");
  const babelify = require("babelify")
  const babel = require("gulp-babel")
  return gulp
    .src("assets/js/*.js")
    .pipe(
      bro({
        transform: [
          babelify.configure({ presets: ["@babel/preset-env"] }),
          ["uglifyify", { global: true }]
        ]
      })
    )
    .pipe(gulp.dest('backend/static/js'));
};

const watch = () => {
  gulp.watch(["assets/scss/*", "assets/scss/*/*", "assets/scss/*/*/*" ], css)
  gulp.watch(["assets/scss/email/*"], email)
  gulp.watch(["assets/js/*"], js)
}


exports.default = gulp.series(css, email, js, watch);