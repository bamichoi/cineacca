import axios from "axios";

const reviewDetailBox = document.querySelector(".review_detail_container");
const deleteBtn = document.querySelector(".delete");
const pk = deleteBtn.value;
const obj = reviewDetailBox.dataset.obj

function handleClickDelete(event){
    event.preventDefault();

    if (confirm("Vuoi veramente eliminare questo review?")) {
        reviewDetailBox.style.display = "none";

        let data = new FormData();

        data.append("pk", pk);
        data.append("object_type", obj);

        axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"; 
        axios.defaults.xsrfCookieName = "csrftoken";

        axios.post("/reviews/api/delete/", data)
        .then(res => {
            alert("Il review è emliminato!")
        })
        .catch(errors => console.log(errors.response.data));

      } 
       
    
}


deleteBtn.addEventListener("click", handleClickDelete);
