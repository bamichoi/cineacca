(function(){function r(e,n,t){function o(i,f){if(!n[i]){if(!e[i]){var c="function"==typeof require&&require;if(!f&&c)return c(i,!0);if(u)return u(i,!0);var a=new Error("Cannot find module '"+i+"'");throw a.code="MODULE_NOT_FOUND",a}var p=n[i]={exports:{}};e[i][0].call(p.exports,function(r){var n=e[i][1][r];return o(n||r)},p,p.exports,r,e,n,t)}return n[i].exports}for(var u="function"==typeof require&&require,i=0;i<t.length;i++)o(t[i]);return o}return r})()({1:[function(require,module,exports){
"use strict";var _regeneratorRuntime=_interopRequireDefault(require("regenerator-runtime")),_ffmpeg=require("@ffmpeg/ffmpeg");function _interopRequireDefault(e){return e&&e.__esModule?e:{default:e}}function asyncGeneratorStep(e,t,n,r,i,a,o){try{var s=e[a](o),d=s.value}catch(e){return void n(e)}s.done?t(d):Promise.resolve(d).then(r,i)}function _asyncToGenerator(e){return function(){var t=this,n=arguments;return new Promise(function(r,i){var a=e.apply(t,n);function o(e){asyncGeneratorStep(a,r,i,o,s,"next",e)}function s(e){asyncGeneratorStep(a,r,i,o,s,"throw",e)}o(void 0)})}}var newFile,percent,videoInput=document.getElementById("id_video"),posterInput=document.getElementById("id_poster"),thumbnailInput=document.getElementById("id_thumbnail"),submitDiv=document.querySelector(".upload_submit"),submitBtn=submitDiv.querySelector("button"),progress=document.getElementById("progress"),progressBar=document.getElementById("progress_bar"),dT=new DataTransfer,handleSizeValidation=function(e){e.target.files[0].size>10485760&&(window.alert("l'immagine si deve essre meno di 10MB"),e.target.value="")},handleCompress=function(){var e=_asyncToGenerator(_regeneratorRuntime.default.mark(function e(t){var n,r,i,a,o,s,d,u,l;return _regeneratorRuntime.default.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:if(n=t.target.files,r=n[0],i=r.name,a=r.size,1572864e3,!(a>1572864e3)){e.next=7;break}return window.alert("Il video orginale si deve essre meno di 1.5GB"),videoInput.value="",e.abrupt("return");case 7:return window.alert("Ora inizia la compresseione video. A seconda dell'ambiente e delle dimesioni del file, potrebbe volerci parecchio tempo. Si prega di evitare di fare un altro lavoro il più possibile. Non appena è finito ti faremo sapre. Si prega di attendere fino al termine del lavoro."),submitBtn.disabled=!0,progress.hidden=!1,submitBtn.style.backgroundColor="#ced6e0",o=i.slice(0,-4),s=(new Date).getTime(),d=o+s+"",u=(0,_ffmpeg.createFFmpeg)({log:!0}),e.next=17,u.load();case 17:return e.t0=u,e.t1=i,e.next=21,(0,_ffmpeg.fetchFile)(n[0]);case 21:return e.t2=e.sent,e.t0.FS.call(e.t0,"writeFile",e.t1,e.t2),u.setProgress(function(e){var t=e.ratio;percent=Math.floor(100*t),progressBar.style.width="".concat(percent,"%"),submitBtn.innerText="Compressing... ".concat(percent,"%")}),e.next=26,u.run("-i",i,"-vcodec","h264","-crf","28","-acodec","mp3","-f","mp4","output.mp4");case 26:l=u.FS("readFile","output.mp4"),newFile=new File([l],d,{type:"video/mp4",lastModified:(new Date).getTime()}),dT.items.length>0&&dT.items.clear(),dT.items.add(newFile),videoInput.files=dT.files,window.alert("La compressione video è finita! Ora puoi caricare video. Grazie per la pazienza."),submitBtn.innerText="Carica",submitBtn.disabled=!1,progress.hidden=!0,submitBtn.style.backgroundColor="#ca5b4c",console.log(videoInput.files[0].size);case 37:case"end":return e.stop()}},e)}));return function(t){return e.apply(this,arguments)}}();videoInput.addEventListener("change",handleCompress),posterInput.addEventListener("change",handleSizeValidation),thumbnailInput.addEventListener("change",handleSizeValidation);

},{"@ffmpeg/ffmpeg":9,"regenerator-runtime":14}],2:[function(require,module,exports){
module.exports={
  "_from": "@ffmpeg/ffmpeg",
  "_id": "@ffmpeg/ffmpeg@0.10.1",
  "_inBundle": false,
  "_integrity": "sha512-ChQkH7Rh57hmVo1LhfQFibWX/xqneolJKSwItwZdKPcLZuKigtYAYDIvB55pDfP17VtR1R77SxgkB2/UApB+Og==",
  "_location": "/@ffmpeg/ffmpeg",
  "_phantomChildren": {},
  "_requested": {
    "type": "tag",
    "registry": true,
    "raw": "@ffmpeg/ffmpeg",
    "name": "@ffmpeg/ffmpeg",
    "escapedName": "@ffmpeg%2fffmpeg",
    "scope": "@ffmpeg",
    "rawSpec": "",
    "saveSpec": null,
    "fetchSpec": "latest"
  },
  "_requiredBy": [
    "#USER",
    "/"
  ],
  "_resolved": "https://registry.npmjs.org/@ffmpeg/ffmpeg/-/ffmpeg-0.10.1.tgz",
  "_shasum": "3dacf3985de9c83a95fbf79fe709920cc009b00a",
  "_spec": "@ffmpeg/ffmpeg",
  "_where": "/Users/bami/Documents/cineacca",
  "author": {
    "name": "Jerome Wu",
    "email": "jeromewus@gmail.com"
  },
  "browser": {
    "./src/node/index.js": "./src/browser/index.js"
  },
  "bugs": {
    "url": "https://github.com/ffmpegwasm/ffmpeg.wasm/issues"
  },
  "bundleDependencies": false,
  "dependencies": {
    "is-url": "^1.2.4",
    "node-fetch": "^2.6.1",
    "regenerator-runtime": "^0.13.7",
    "resolve-url": "^0.2.1"
  },
  "deprecated": false,
  "description": "FFmpeg WebAssembly version",
  "devDependencies": {
    "@babel/core": "^7.12.3",
    "@babel/preset-env": "^7.12.1",
    "@ffmpeg/core": "^0.10.0",
    "@types/emscripten": "^1.39.4",
    "babel-loader": "^8.1.0",
    "chai": "^4.2.0",
    "cors": "^2.8.5",
    "eslint": "^7.12.1",
    "eslint-config-airbnb-base": "^14.1.0",
    "eslint-plugin-import": "^2.22.1",
    "express": "^4.17.1",
    "mocha": "^8.2.1",
    "mocha-headless-chrome": "^2.0.3",
    "npm-run-all": "^4.1.5",
    "wait-on": "^5.3.0",
    "webpack": "^5.3.2",
    "webpack-cli": "^4.1.0",
    "webpack-dev-middleware": "^4.0.0"
  },
  "directories": {
    "example": "examples"
  },
  "engines": {
    "node": ">=12.16.1"
  },
  "homepage": "https://github.com/ffmpegwasm/ffmpeg.wasm#readme",
  "keywords": [
    "ffmpeg",
    "WebAssembly",
    "video"
  ],
  "license": "MIT",
  "main": "src/index.js",
  "name": "@ffmpeg/ffmpeg",
  "repository": {
    "type": "git",
    "url": "git+https://github.com/ffmpegwasm/ffmpeg.wasm.git"
  },
  "scripts": {
    "build": "rimraf dist && webpack --config scripts/webpack.config.prod.js",
    "lint": "eslint src",
    "prepublishOnly": "npm run build",
    "start": "node scripts/server.js",
    "test": "npm-run-all -p -r start test:all",
    "test:all": "npm-run-all wait test:browser:ffmpeg test:node:all",
    "test:browser": "mocha-headless-chrome -a allow-file-access-from-files -a incognito -a no-sandbox -a disable-setuid-sandbox -a disable-logging -t 300000",
    "test:browser:ffmpeg": "npm run test:browser -- -f ./tests/ffmpeg.test.html",
    "test:node": "node --experimental-wasm-threads --experimental-wasm-bulk-memory node_modules/.bin/_mocha --exit --bail --require ./scripts/test-helper.js",
    "test:node:all": "npm run test:node -- ./tests/*.test.js",
    "wait": "rimraf dist && wait-on http://localhost:3000/dist/ffmpeg.dev.js"
  },
  "types": "src/index.d.ts",
  "version": "0.10.1"
}

},{}],3:[function(require,module,exports){
(function (process){(function (){
const resolveURL=require("resolve-url"),{devDependencies:devDependencies}=require("../../package.json");module.exports={corePath:"development"===process.env.NODE_ENV?resolveURL("/node_modules/@ffmpeg/core/dist/ffmpeg-core.js"):`https://unpkg.com/@ffmpeg/core@${devDependencies["@ffmpeg/core"].substring(1)}/dist/ffmpeg-core.js`};

}).call(this)}).call(this,require('_process'))
},{"../../package.json":2,"_process":13,"resolve-url":15}],4:[function(require,module,exports){
const resolveURL=require("resolve-url"),readFromBlobOrFile=e=>new Promise((r,a)=>{const o=new FileReader;o.onload=(()=>{r(o.result)}),o.onerror=(({target:{error:{code:e}}})=>{a(Error(`File could not be read! Code=${e}`))}),o.readAsArrayBuffer(e)});module.exports=(async e=>{let r=e;if(void 0===e)return new Uint8Array;if("string"==typeof e)if(/data:_data\/([a-zA-Z]*);base64,([^"]*)/.test(e))r=atob(e.split(",")[1]).split("").map(e=>e.charCodeAt(0));else{const a=await fetch(resolveURL(e));r=await a.arrayBuffer()}else(e instanceof File||e instanceof Blob)&&(r=await readFromBlobOrFile(e));return new Uint8Array(r)});

},{"resolve-url":15}],5:[function(require,module,exports){
const resolveURL=require("resolve-url"),{log:log}=require("../utils/log"),toBlobURL=async(e,o)=>{log("info",`fetch ${e}`);const r=await(await fetch(e)).arrayBuffer();log("info",`${e} file size = ${r.byteLength} bytes`);const t=new Blob([r],{type:o}),a=URL.createObjectURL(t);return log("info",`${e} blob URL = ${a}`),a};module.exports=(async({corePath:e})=>{if("string"!=typeof e)throw Error("corePath should be a string!");const o=resolveURL(e),r=await toBlobURL(o,"application/javascript"),t=await toBlobURL(o.replace("ffmpeg-core.js","ffmpeg-core.wasm"),"application/wasm"),a=await toBlobURL(o.replace("ffmpeg-core.js","ffmpeg-core.worker.js"),"application/javascript");return"undefined"==typeof createFFmpegCore?new Promise(e=>{const o=document.createElement("script"),c=()=>{o.removeEventListener("load",c),log("info","ffmpeg-core.js script loaded"),e({createFFmpegCore:createFFmpegCore,corePath:r,wasmPath:t,workerPath:a})};o.src=r,o.type="text/javascript",o.addEventListener("load",c),document.getElementsByTagName("head")[0].appendChild(o)}):(log("info","ffmpeg-core.js script is loaded already"),Promise.resolve({createFFmpegCore:createFFmpegCore,corePath:r,wasmPath:t,workerPath:a}))});

},{"../utils/log":10,"resolve-url":15}],6:[function(require,module,exports){
const defaultOptions=require("./defaultOptions"),getCreateFFmpegCore=require("./getCreateFFmpegCore"),fetchFile=require("./fetchFile");module.exports={defaultOptions:defaultOptions,getCreateFFmpegCore:getCreateFFmpegCore,fetchFile:fetchFile};

},{"./defaultOptions":3,"./fetchFile":4,"./getCreateFFmpegCore":5}],7:[function(require,module,exports){
module.exports={defaultArgs:["./ffmpeg","-nostdin","-y"],baseOptions:{log:!1,logger:()=>{},progress:()=>{},corePath:""}};

},{}],8:[function(require,module,exports){
const{defaultArgs:defaultArgs,baseOptions:baseOptions}=require("./config"),{setLogging:setLogging,setCustomLogger:setCustomLogger,log:log}=require("./utils/log"),parseProgress=require("./utils/parseProgress"),parseArgs=require("./utils/parseArgs"),{defaultOptions:defaultOptions,getCreateFFmpegCore:getCreateFFmpegCore}=require("./node"),{version:version}=require("../package.json"),NO_LOAD=Error("ffmpeg.wasm is not ready, make sure you have completed load().");module.exports=((e={})=>{const{log:r,logger:o,progress:t,...s}={...baseOptions,...defaultOptions,...e};let n=null,g=null,i=null,a=!1,l=t;const f=({type:e,message:r})=>{log(e,r),parseProgress(r,l),(e=>{"FFMPEG_END"===e&&null!==i&&(i(),i=null,a=!1)})(r)};return setLogging(r),setCustomLogger(o),log("info",`use ffmpeg.wasm v${version}`),{setProgress:e=>{l=e},setLogger:e=>{setCustomLogger(e)},setLogging:setLogging,load:async()=>{if(log("info","load ffmpeg-core"),null!==n)throw Error("ffmpeg.wasm was loaded, you should not load it again, use ffmpeg.isLoaded() to check next time.");{log("info","loading ffmpeg-core");const{createFFmpegCore:e,corePath:r,workerPath:o,wasmPath:t}=await getCreateFFmpegCore(s);n=await e({mainScriptUrlOrBlob:r,printErr:e=>f({type:"fferr",message:e}),print:e=>f({type:"ffout",message:e}),locateFile:(e,r)=>{if("undefined"!=typeof window){if(void 0!==t&&e.endsWith("ffmpeg-core.wasm"))return t;if(void 0!==o&&e.endsWith("ffmpeg-core.worker.js"))return o}return r+e}}),g=n.cwrap("proxy_main","number",["number","number"]),log("info","ffmpeg-core loaded")}},isLoaded:()=>null!==n,run:(...e)=>{if(log("info",`run ffmpeg command: ${e.join(" ")}`),null===n)throw NO_LOAD;if(a)throw Error("ffmpeg.wasm can only run one command at a time");return a=!0,new Promise(r=>{const o=[...defaultArgs,...e].filter(e=>0!==e.length);i=r,g(...parseArgs(n,o))})},exit:()=>{if(null===n)throw NO_LOAD;a=!1,n.exit(1),n=null,g=null,i=null},FS:(e,...r)=>{if(log("info",`run FS.${e} ${r.map(e=>"string"==typeof e?e:`<${e.length} bytes binary file>`).join(" ")}`),null===n)throw NO_LOAD;{let o=null;try{o=n.FS[e](...r)}catch(o){throw"readdir"===e?Error(`ffmpeg.FS('readdir', '${r[0]}') error. Check if the path exists, ex: ffmpeg.FS('readdir', '/')`):"readFile"===e?Error(`ffmpeg.FS('readFile', '${r[0]}') error. Check if the path exists`):Error("Oops, something went wrong in FS operation.")}return o}}}});

},{"../package.json":2,"./config":7,"./node":6,"./utils/log":10,"./utils/parseArgs":11,"./utils/parseProgress":12}],9:[function(require,module,exports){
require("regenerator-runtime/runtime");const createFFmpeg=require("./createFFmpeg"),{fetchFile:fetchFile}=require("./node");module.exports={createFFmpeg:createFFmpeg,fetchFile:fetchFile};

},{"./createFFmpeg":8,"./node":6,"regenerator-runtime/runtime":14}],10:[function(require,module,exports){
let logging=!1,customLogger=()=>{};const setLogging=g=>{logging=g},setCustomLogger=g=>{customLogger=g},log=(g,o)=>{customLogger({type:g,message:o}),logging&&console.log(`[${g}] ${o}`)};module.exports={logging:logging,setLogging:setLogging,setCustomLogger:setCustomLogger,log:log};

},{}],11:[function(require,module,exports){
module.exports=((t,E)=>{const e=t._malloc(E.length*Uint32Array.BYTES_PER_ELEMENT);return E.forEach((E,r)=>{const l=t._malloc(E.length+1);t.writeAsciiToMemory(E,l),t.setValue(e+Uint32Array.BYTES_PER_ELEMENT*r,l,"i32")}),[E.length,e]});

},{}],12:[function(require,module,exports){
let duration=0,ratio=0;const ts2sec=t=>{const[i,s,r]=t.split(":");return 60*parseFloat(i)*60+60*parseFloat(s)+parseFloat(r)};module.exports=((t,i)=>{if("string"==typeof t)if(t.startsWith("  Duration")){const s=t.split(", ")[0].split(": ")[1],r=ts2sec(s);i({duration:r,ratio:ratio}),(0===duration||duration>r)&&(duration=r)}else if(t.startsWith("frame")||t.startsWith("size")){const s=t.split("time=")[1].split(" ")[0],r=ts2sec(s);i({ratio:ratio=r/duration,time:r})}else t.startsWith("video:")&&(i({ratio:1}),duration=0)});

},{}],13:[function(require,module,exports){
var cachedSetTimeout,cachedClearTimeout,process=module.exports={};function defaultSetTimout(){throw new Error("setTimeout has not been defined")}function defaultClearTimeout(){throw new Error("clearTimeout has not been defined")}function runTimeout(e){if(cachedSetTimeout===setTimeout)return setTimeout(e,0);if((cachedSetTimeout===defaultSetTimout||!cachedSetTimeout)&&setTimeout)return cachedSetTimeout=setTimeout,setTimeout(e,0);try{return cachedSetTimeout(e,0)}catch(t){try{return cachedSetTimeout.call(null,e,0)}catch(t){return cachedSetTimeout.call(this,e,0)}}}function runClearTimeout(e){if(cachedClearTimeout===clearTimeout)return clearTimeout(e);if((cachedClearTimeout===defaultClearTimeout||!cachedClearTimeout)&&clearTimeout)return cachedClearTimeout=clearTimeout,clearTimeout(e);try{return cachedClearTimeout(e)}catch(t){try{return cachedClearTimeout.call(null,e)}catch(t){return cachedClearTimeout.call(this,e)}}}!function(){try{cachedSetTimeout="function"==typeof setTimeout?setTimeout:defaultSetTimout}catch(e){cachedSetTimeout=defaultSetTimout}try{cachedClearTimeout="function"==typeof clearTimeout?clearTimeout:defaultClearTimeout}catch(e){cachedClearTimeout=defaultClearTimeout}}();var currentQueue,queue=[],draining=!1,queueIndex=-1;function cleanUpNextTick(){draining&&currentQueue&&(draining=!1,currentQueue.length?queue=currentQueue.concat(queue):queueIndex=-1,queue.length&&drainQueue())}function drainQueue(){if(!draining){var e=runTimeout(cleanUpNextTick);draining=!0;for(var t=queue.length;t;){for(currentQueue=queue,queue=[];++queueIndex<t;)currentQueue&&currentQueue[queueIndex].run();queueIndex=-1,t=queue.length}currentQueue=null,draining=!1,runClearTimeout(e)}}function Item(e,t){this.fun=e,this.array=t}function noop(){}process.nextTick=function(e){var t=new Array(arguments.length-1);if(arguments.length>1)for(var r=1;r<arguments.length;r++)t[r-1]=arguments[r];queue.push(new Item(e,t)),1!==queue.length||draining||runTimeout(drainQueue)},Item.prototype.run=function(){this.fun.apply(null,this.array)},process.title="browser",process.browser=!0,process.env={},process.argv=[],process.version="",process.versions={},process.on=noop,process.addListener=noop,process.once=noop,process.off=noop,process.removeListener=noop,process.removeAllListeners=noop,process.emit=noop,process.prependListener=noop,process.prependOnceListener=noop,process.listeners=function(e){return[]},process.binding=function(e){throw new Error("process.binding is not supported")},process.cwd=function(){return"/"},process.chdir=function(e){throw new Error("process.chdir is not supported")},process.umask=function(){return 0};

},{}],14:[function(require,module,exports){
var runtime=function(t){"use strict";var r,e=Object.prototype,n=e.hasOwnProperty,o="function"==typeof Symbol?Symbol:{},i=o.iterator||"@@iterator",a=o.asyncIterator||"@@asyncIterator",c=o.toStringTag||"@@toStringTag";function u(t,r,e){return Object.defineProperty(t,r,{value:e,enumerable:!0,configurable:!0,writable:!0}),t[r]}try{u({},"")}catch(t){u=function(t,r,e){return t[r]=e}}function h(t,r,e,n){var o=r&&r.prototype instanceof g?r:g,i=Object.create(o.prototype),a=new G(n||[]);return i._invoke=function(t,r,e){var n=l;return function(o,i){if(n===p)throw new Error("Generator is already running");if(n===y){if("throw"===o)throw i;return T()}for(e.method=o,e.arg=i;;){var a=e.delegate;if(a){var c=j(a,e);if(c){if(c===v)continue;return c}}if("next"===e.method)e.sent=e._sent=e.arg;else if("throw"===e.method){if(n===l)throw n=y,e.arg;e.dispatchException(e.arg)}else"return"===e.method&&e.abrupt("return",e.arg);n=p;var u=f(t,r,e);if("normal"===u.type){if(n=e.done?y:s,u.arg===v)continue;return{value:u.arg,done:e.done}}"throw"===u.type&&(n=y,e.method="throw",e.arg=u.arg)}}}(t,e,a),i}function f(t,r,e){try{return{type:"normal",arg:t.call(r,e)}}catch(t){return{type:"throw",arg:t}}}t.wrap=h;var l="suspendedStart",s="suspendedYield",p="executing",y="completed",v={};function g(){}function d(){}function m(){}var w={};u(w,i,function(){return this});var L=Object.getPrototypeOf,x=L&&L(L(N([])));x&&x!==e&&n.call(x,i)&&(w=x);var b=m.prototype=g.prototype=Object.create(w);function E(t){["next","throw","return"].forEach(function(r){u(t,r,function(t){return this._invoke(r,t)})})}function _(t,r){var e;this._invoke=function(o,i){function a(){return new r(function(e,a){!function e(o,i,a,c){var u=f(t[o],t,i);if("throw"!==u.type){var h=u.arg,l=h.value;return l&&"object"==typeof l&&n.call(l,"__await")?r.resolve(l.__await).then(function(t){e("next",t,a,c)},function(t){e("throw",t,a,c)}):r.resolve(l).then(function(t){h.value=t,a(h)},function(t){return e("throw",t,a,c)})}c(u.arg)}(o,i,e,a)})}return e=e?e.then(a,a):a()}}function j(t,e){var n=t.iterator[e.method];if(n===r){if(e.delegate=null,"throw"===e.method){if(t.iterator.return&&(e.method="return",e.arg=r,j(t,e),"throw"===e.method))return v;e.method="throw",e.arg=new TypeError("The iterator does not provide a 'throw' method")}return v}var o=f(n,t.iterator,e.arg);if("throw"===o.type)return e.method="throw",e.arg=o.arg,e.delegate=null,v;var i=o.arg;return i?i.done?(e[t.resultName]=i.value,e.next=t.nextLoc,"return"!==e.method&&(e.method="next",e.arg=r),e.delegate=null,v):i:(e.method="throw",e.arg=new TypeError("iterator result is not an object"),e.delegate=null,v)}function O(t){var r={tryLoc:t[0]};1 in t&&(r.catchLoc=t[1]),2 in t&&(r.finallyLoc=t[2],r.afterLoc=t[3]),this.tryEntries.push(r)}function k(t){var r=t.completion||{};r.type="normal",delete r.arg,t.completion=r}function G(t){this.tryEntries=[{tryLoc:"root"}],t.forEach(O,this),this.reset(!0)}function N(t){if(t){var e=t[i];if(e)return e.call(t);if("function"==typeof t.next)return t;if(!isNaN(t.length)){var o=-1,a=function e(){for(;++o<t.length;)if(n.call(t,o))return e.value=t[o],e.done=!1,e;return e.value=r,e.done=!0,e};return a.next=a}}return{next:T}}function T(){return{value:r,done:!0}}return d.prototype=m,u(b,"constructor",m),u(m,"constructor",d),d.displayName=u(m,c,"GeneratorFunction"),t.isGeneratorFunction=function(t){var r="function"==typeof t&&t.constructor;return!!r&&(r===d||"GeneratorFunction"===(r.displayName||r.name))},t.mark=function(t){return Object.setPrototypeOf?Object.setPrototypeOf(t,m):(t.__proto__=m,u(t,c,"GeneratorFunction")),t.prototype=Object.create(b),t},t.awrap=function(t){return{__await:t}},E(_.prototype),u(_.prototype,a,function(){return this}),t.AsyncIterator=_,t.async=function(r,e,n,o,i){void 0===i&&(i=Promise);var a=new _(h(r,e,n,o),i);return t.isGeneratorFunction(e)?a:a.next().then(function(t){return t.done?t.value:a.next()})},E(b),u(b,c,"Generator"),u(b,i,function(){return this}),u(b,"toString",function(){return"[object Generator]"}),t.keys=function(t){var r=[];for(var e in t)r.push(e);return r.reverse(),function e(){for(;r.length;){var n=r.pop();if(n in t)return e.value=n,e.done=!1,e}return e.done=!0,e}},t.values=N,G.prototype={constructor:G,reset:function(t){if(this.prev=0,this.next=0,this.sent=this._sent=r,this.done=!1,this.delegate=null,this.method="next",this.arg=r,this.tryEntries.forEach(k),!t)for(var e in this)"t"===e.charAt(0)&&n.call(this,e)&&!isNaN(+e.slice(1))&&(this[e]=r)},stop:function(){this.done=!0;var t=this.tryEntries[0].completion;if("throw"===t.type)throw t.arg;return this.rval},dispatchException:function(t){if(this.done)throw t;var e=this;function o(n,o){return c.type="throw",c.arg=t,e.next=n,o&&(e.method="next",e.arg=r),!!o}for(var i=this.tryEntries.length-1;i>=0;--i){var a=this.tryEntries[i],c=a.completion;if("root"===a.tryLoc)return o("end");if(a.tryLoc<=this.prev){var u=n.call(a,"catchLoc"),h=n.call(a,"finallyLoc");if(u&&h){if(this.prev<a.catchLoc)return o(a.catchLoc,!0);if(this.prev<a.finallyLoc)return o(a.finallyLoc)}else if(u){if(this.prev<a.catchLoc)return o(a.catchLoc,!0)}else{if(!h)throw new Error("try statement without catch or finally");if(this.prev<a.finallyLoc)return o(a.finallyLoc)}}}},abrupt:function(t,r){for(var e=this.tryEntries.length-1;e>=0;--e){var o=this.tryEntries[e];if(o.tryLoc<=this.prev&&n.call(o,"finallyLoc")&&this.prev<o.finallyLoc){var i=o;break}}i&&("break"===t||"continue"===t)&&i.tryLoc<=r&&r<=i.finallyLoc&&(i=null);var a=i?i.completion:{};return a.type=t,a.arg=r,i?(this.method="next",this.next=i.finallyLoc,v):this.complete(a)},complete:function(t,r){if("throw"===t.type)throw t.arg;return"break"===t.type||"continue"===t.type?this.next=t.arg:"return"===t.type?(this.rval=this.arg=t.arg,this.method="return",this.next="end"):"normal"===t.type&&r&&(this.next=r),v},finish:function(t){for(var r=this.tryEntries.length-1;r>=0;--r){var e=this.tryEntries[r];if(e.finallyLoc===t)return this.complete(e.completion,e.afterLoc),k(e),v}},catch:function(t){for(var r=this.tryEntries.length-1;r>=0;--r){var e=this.tryEntries[r];if(e.tryLoc===t){var n=e.completion;if("throw"===n.type){var o=n.arg;k(e)}return o}}throw new Error("illegal catch attempt")},delegateYield:function(t,e,n){return this.delegate={iterator:N(t),resultName:e,nextLoc:n},"next"===this.method&&(this.arg=r),v}},t}("object"==typeof module?module.exports:{});try{regeneratorRuntime=runtime}catch(t){"object"==typeof globalThis?globalThis.regeneratorRuntime=runtime:Function("r","regeneratorRuntime = r")(runtime)}

},{}],15:[function(require,module,exports){
!function(e,r){"function"==typeof define&&define.amd?define(r):"object"==typeof exports?module.exports=r():e.resolveUrl=r()}(this,function(){return function(){var e=arguments.length;if(0===e)throw new Error("resolveUrl requires at least one argument; got none.");var r=document.createElement("base");if(r.href=arguments[0],1===e)return r.href;var t=document.getElementsByTagName("head")[0];t.insertBefore(r,t.firstChild);for(var n,o=document.createElement("a"),f=1;f<e;f++)o.href=arguments[f],n=o.href,r.href=n;return t.removeChild(r),n}});

},{}]},{},[1]);
