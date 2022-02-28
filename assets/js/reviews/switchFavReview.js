import axios from "axios";

const reviewLikeItDivs = document.getElementsByClassName("review_like_it");

const handleClickLikeIt = (event, div) => {
  const reviewLikeItIco = event.target; // !) 왜 div가 아니라 i로 찍히는지..
  const reviewPk = div.dataset.pk;
  const state = div.dataset.state;
  const objType = div.dataset.obj;
  const numFav = div.querySelector("span");

  let handleType = null;
  if (state == "empty") {
    handleType = "add";
  } else {
    handleType = "remove";
  }

  let data = new FormData();

  axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
  axios.defaults.xsrfCookieName = "csrftoken";

  data.append("handleType", handleType);
  data.append("objType", objType);

  axios
    .post(`/reviews/api/${reviewPk}/fav/`, data)
    .then((res) => {
      const result = res.data.result;
      const numFavUsers = res.data.numFavUsers;
      if (result == "added") {
        reviewLikeItIco.className = "fas fa-heart";
        div.dataset.state = "filled";
      } else {
        reviewLikeItIco.className = "far fa-heart";
        div.dataset.state = "empty";
      }
      numFav.innerText = `${numFavUsers}`;
    })
    .catch((errors) => console.log(errors.response.data));
};

for (const reviewLikeItDiv of reviewLikeItDivs) {
  const reviewLikeItBtn = reviewLikeItDiv.querySelector(".review_like_it_btn");
  reviewLikeItBtn.addEventListener("click", (event) => {
    handleClickLikeIt(event, reviewLikeItDiv);
  });
}
