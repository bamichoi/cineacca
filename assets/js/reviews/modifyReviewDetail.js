import axios from "axios";

const modifyBtn = document.querySelector(".modify");
const updateBtn = document.querySelector(".update");
const cancelBtn = document.querySelector(".cancel");

function handleClickModify(event) {

    const modifyBtn = event.target;
    const pk = modifyBtn.value;
    
}



modifyBtn.addEventListener("click", handleClickModify);