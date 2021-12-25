import videojs from "video.js";

const movieInfo = document.querySelector(".detail_movieInfo");
const thumbnail = movieInfo.dataset.thumb;

const options = {
    controls: true,
    preload:"metadata",
    fluid:true,
    //poster:thumbnail
};
//to do: breakpoints (responsive option)

videojs('videoPlayer', options);    

videojs.log.level('error');