import axios from "axios";

const reviewForm = document.getElementById("review_form");
const reviewContainer = document.querySelector(".reviewForm_container");
const moviePk = reviewContainer.dataset.pk


    function handelSubmitReview(event) {
        event.preventDefault();
        const titleInput = reviewForm.querySelector("#review_title");
        const rateInput = reviewForm.querySelector("#review_rate");
        const stars = reviewForm.querySelector(".full_stars");
        const score = reviewForm.querySelector("#score");
        const contentInput = reviewForm.querySelector("#review_content");

        let data = new FormData(); // !) const가 아니라 let 이어야하는 이유?

        const reviewTitle = titleInput.value;
        const reviewRate = rateInput.value;
        const reviewContent = contentInput.value;
        const object_type = "movie"

        titleInput.value = "";
        rateInput.value = "";
        contentInput.value = "";
        stars.style.width = 0;
        score.innerText = '"0.0"'

        axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"; 
        axios.defaults.xsrfCookieName = "csrftoken";

        data.append("title", reviewTitle);
        data.append("rate", reviewRate);
        data.append("content", reviewContent);
        data.append("object_type", object_type);  
        
        axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"; 
        axios.defaults.xsrfCookieName = "csrftoken";
        
        axios.post(`/api/${moviePk}/review/create/`, data)
            .then(res => {
                const pk = res.data.pk;
                const title = res.data.title;
                const rate = res.data.rate;
                const content = res.data.content;
                const created =  res.data.created;
              
                const reviewsUl = document.getElementById("reviews");
                const newReview = reviewsUl.querySelector(".new_review");
                const newReviewTitle = newReview.querySelector(".review_title");
                const newReviewRate = newReview.querySelector(".review_rate");
                const newReviewContent = newReview.querySelector(".review_content");
                const newReviewDate = newReview.querySelector(".review_box__date");
                const likeItDiv = newReview.querySelector(".review_like_it");
                const numFav = likeItDiv.querySelector("span");

                newReview.setAttribute("id", `${pk}`);
                const reviewBtns = newReview.querySelector(".review_btns")
                const modifyBtn = newReview.querySelector(".modify");
                const deleteBtn = newReview.querySelector(".delete");
                const modifyForm = newReview.querySelector(".modify_form");
                const modifyTitle = modifyForm.querySelector(".modify_title");
                const modifyRate = modifyForm.querySelector(".modify_rate");
                const modifyScore = modifyForm.querySelector(".modify_score");
                const modifyContent = modifyForm.querySelector(".modify_content");
                 

 
                newReviewTitle.innerText = `${title}`;
                newReviewRate.innerText =  rate.includes(".") ? `"${rate}"` : `"${rate}.0"`
                newReviewContent.innerText = `${content}`;
                reviewBtns.style.display = "flex"
                modifyBtn.setAttribute("value", `${pk}`);
                deleteBtn.setAttribute("value", `${pk}`);
                newReviewDate.innerText = `${created}`;
                likeItDiv.setAttribute("data-pk", `${pk}`); 
                numFav.innerText = "0"

             
                modifyScore.innerText = rate.includes(".") ? `rating: "${rate}"` : `rating: "${rate}.0"`
                modifyTitle.setAttribute("value", `${title}`);
                modifyRate.setAttribute("value", `${rate}`);
                modifyContent.innerText = `${content}`;

                newReview.hidden = false;

            })
            .catch(errors => console.log(errors.response.data))
    
        
    }

    reviewForm.addEventListener("submit", handelSubmitReview)