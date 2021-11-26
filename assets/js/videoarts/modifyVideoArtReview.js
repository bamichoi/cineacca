import axios from "axios";

const modifyBtns = document.getElementsByClassName("modify");
const updateBtns = document.getElementsByClassName("update");
const cancelBtns = document.getElementsByClassName("cancel");


function handleClickModify(event) {

    const modifyBtn = event.target;
    const pk = modifyBtn.value;
    const reviewLi = document.getElementById(`${pk}`);
    const reviewBox = reviewLi.querySelector(".review_box");  
    const contentContainer = reviewBox.querySelector(".review_box__content_container")
    const userContainer = reviewBox.querySelector(".review_box__user_container")
    const modifyBox = reviewLi.querySelector(".modify_box");
    const modifyForm = reviewLi.querySelector(".modify_form");
    const modiRateInputs = reviewLi.getElementsByClassName("modify_rate");
    const modiScore = reviewLi.querySelector(".modify_score_text")
    const modiEmptyStars = reviewLi.getElementsByClassName("modify_empty_stars");
    const modiFullStars = reviewLi.querySelector(".modify_full_stars")
    const cancelBtn = reviewLi.querySelector(".cancel");
    const updateBtn = reviewLi.querySelector(".update");

    const handleModiOninput = (event) => {
        const { value } = event.target
        const convertValue = value * 20 + "%"
        modiFullStars.style.width = convertValue
        modiScore.innerText = value.includes(".") ? `rating: "${value}"` : `rating: "${value}.0"`
    }

    reviewBox.style.display = "none"; //hidden이 작동안되는 이유?
    modifyBox.style.display = "flex";
    

    for ( const modiRateInput of modiRateInputs) {
        modiRateInput.addEventListener("input", handleModiOninput)
        modiFullStars.style.width = modiRateInput.value * 20 + "%"
    } 

    // cancel 버튼을 누를 때
    cancelBtn.addEventListener("click", (event) => {
        event.preventDefault();
        reviewBox.style.display = "flex";
        modifyBox.style.display = "none";
    })

    // update 버튼으로 form을 submit할때 
    modifyForm.addEventListener("submit", (event) => {
        event.preventDefault();
        const titleInput = modifyForm.querySelector(".modify_title");
        const rateInput = modifyForm.querySelector(".modify_rate");
        const contentInput = modifyForm.querySelector(".modify_content");
        const reviewTitle = contentContainer.querySelector(".review_title");
        const reviewRate = userContainer.querySelector(".review_rate");
        const reviewContent = contentContainer.querySelector(".review_content");
        const updateTitle = titleInput.value;
        const updateRate = rateInput.value;
        const updateContent = contentInput.value;
        const object_type = "videoart";

        let data = new FormData(); 
        
        reviewTitle.innerText = `${updateTitle}`;
        reviewRate.innerText = updateRate.includes(".") ? `"${updateRate}"` : `"${updateRate}.0"`
        reviewContent.innerText = `${updateContent}`;

        reviewBox.style.display = "flex";
        modifyBox.style.display = "none";

        data.append("pk", pk);
        data.append("title", updateTitle);
        data.append("rate", updateRate);
        data.append("content", updateContent);
        data.append("object_type", object_type);

        axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"; 
        axios.defaults.xsrfCookieName = "csrftoken";

        axios.post("/reviews/api/review/update/", data)
        .then(res => alert("Il review è modificato."))
        .catch(errors => console.log(errors.response.data));
        
    });
    
    
}

for (const modifyBtn of  modifyBtns) {
    modifyBtn.addEventListener("click", handleClickModify);
}