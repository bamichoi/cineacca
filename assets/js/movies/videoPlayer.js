import videojs from "video.js";
import "videojs-hotkeys";

const movieInfo = document.querySelector(".detail_movieInfo");
const thumbnailUrl = movieInfo.dataset.thumb;

const options = {
  controls: true,
  preload: "metadata",
  fluid: true,
  poster: thumbnailUrl,
};
//to do: breakpoints (responsive option)

videojs("videoPlayer", options);

videojs("videoPlayer").ready(function () {
  this.hotkeys({
    volumeStep: 0.1,
    seekStep: 5,
    enableModifiersForNumbers: false,
  });
});

videojs.log.level("error");
