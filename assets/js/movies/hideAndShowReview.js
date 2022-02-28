const hiddenReviews = document.getElementsByClassName("hidden_review");
const allReivewBtn = document.getElementById("show_all_reviews_btn");

const handleShowAllReviews = () => {
  allReivewBtn.style.display = "none"; // !) 태그 달고나서  hidden 안되는 이유 좀.
  for (const hiddenReview of hiddenReviews) {
    hiddenReview.hidden = false;
  }
};

allReivewBtn.addEventListener("click", handleShowAllReviews);
