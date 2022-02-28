import axios from "axios";

const modifyForm = document.querySelector(".review_detail_modify_form");
const modifyBtn = document.querySelector(".modify");
const updateBtn = document.querySelector(".update");
const cancelBtn = document.querySelector(".cancel");
const reviewDetailBox = document.querySelector(".review_detail_container");
const reviewModifyBox = document.querySelector(".modify_detail_container");
const reviewTitle = document.querySelector(".review_detail__title");
const reviewRate = document
  .querySelector(".review_detail__rating")
  .querySelector("span");
const reviewContent = document.querySelector(".review_detail__content");
const pk = modifyBtn.value;
const obj = reviewDetailBox.dataset.obj;

function handleClickModify(event) {
  const modiRateInput = document.querySelector(".modify_rate");
  const modiFullStars = document.querySelector(".modify_full_stars");

  reviewDetailBox.style.display = "none";
  reviewModifyBox.style.display = "flex";
  modiFullStars.style.width = modiRateInput.value * 20 + "%";

  const handleModiOninput = (event) => {
    const { value } = event.target;
    const convertValue = value * 20 + "%";
    modiFullStars.style.width = convertValue;
  };

  modiRateInput.addEventListener("input", handleModiOninput);

  cancelBtn.addEventListener("click", (event) => {
    event.preventDefault();
    reviewDetailBox.style.display = "flex";
    reviewModifyBox.style.display = "none";
  });

  modifyForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const titleInput = modifyForm.querySelector(".modify_title");
    const rateInput = modifyForm.querySelector(".modify_rate");
    const contentInput = modifyForm.querySelector(".modify_content");
    const updateTitle = titleInput.value;
    const updateRate = rateInput.value;
    const updateContent = contentInput.value;
    const object_type = obj;

    reviewTitle.innerText = `"${updateTitle}"`;
    reviewRate.innerText = updateRate.includes(".")
      ? `${updateRate}`
      : `${updateRate}.0`;
    reviewContent.innerText = `${updateContent}`;

    reviewDetailBox.style.display = "flex";
    reviewModifyBox.style.display = "none";

    let data = new FormData();

    data.append("pk", pk);
    data.append("title", updateTitle);
    data.append("rate", updateRate);
    data.append("content", updateContent);
    data.append("object_type", object_type);

    axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
    axios.defaults.xsrfCookieName = "csrftoken";

    axios
      .post("/reviews/api/update/", data)
      .then((res) => alert("la review è modificata."))
      .catch((errors) => console.log(errors.response.data));
  });
}

modifyBtn.addEventListener("click", handleClickModify);
