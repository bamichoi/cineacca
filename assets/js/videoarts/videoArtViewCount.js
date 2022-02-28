import axios from "axios";

const reviewContainer = document.querySelector(".reviewForm_container");
const videoArtPk = reviewContainer.dataset.pk;

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

let data = new FormData();

axios
  .post(`/videoarts/api/${videoArtPk}/view/`, data) // !)  pk를 굳이 url에 담을 필요가 없었는데
  .then((res) => {
    return;
  })
  .catch((errors) => console.log(errors.response.data));
