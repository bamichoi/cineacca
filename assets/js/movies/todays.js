import regeneratorRuntime from "regenerator-runtime";

const todayLink = document.getElementById("today-movies_link");
const todayVideos = document.getElementsByClassName("today-movies_content");

let todayUrls = [];

for (const todayVideo of todayVideos) {
  const videoUrl = todayVideo.dataset.url;
  todayUrls.push(videoUrl);
}

const timer = (ms) => new Promise((res) => setInterval(res, ms));

const changeTodayUrl = async () => {
  while (true) {
    for (const todayUrl of todayUrls) {
      todayLink.setAttribute("href", todayUrl);
      await timer(6000);
    }
  }
};

changeTodayUrl();
