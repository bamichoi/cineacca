import videojs from "video.js";

const movieInfo = document.querySelector(".detail_movieInfo");
const thumbnailUrl = movieInfo.dataset.thumb;
const videoPlayer = document.querySelector("#videoPlayer_html5_api")
const thumbnailImg = document.createElement('img');

thumbnailImg.classList.add("vjs-poster", "vjs-hidden");
thumbnailImg.setAttribute("tabindex", "-1");
thumbnailImg.setAttribute("aria-disabled", "false");
thumbnailImg.setAttribute("crossorigin", "anonymous");

console.log(thumbnailImg)


const options = {
    controls: true,
    preload:"metadata",
    fluid:true,
};
//to do: breakpoints (responsive option)

videojs('videoPlayer', options);    

videojs.log.level('error');