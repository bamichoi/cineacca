import axios from "axios";

const deleteBtns = document.getElementsByClassName("delete");
const reviewForm = document.getElementById("review_form");
const csrftoken = reviewForm.csrfmiddlewaretoken.value

    function handleClickDelete(event){
        event.preventDefault();
        const deleteBtn = event.target;
        const pk = deleteBtn.value;
        const review = document.getElementById(`${pk}`);
        const object_type = "movie"
        if (confirm("Vuoi veramente eliminare questo review?")) {
            review.hidden = true;

            let data = new FormData();

            data.append("pk", pk);
            data.append("object_type", object_type);
            data.append("csrfmiddlewaretoken", csrftoken); // !) 리뷰폼의 token을 넣어주는게 맞는지 모르겠다..

            axios.post("/api/review/delete/", data)
            .then(res => alert("Il review è emliminato!"))
            .catch(errors => console.log(errors.response.data));

          } 
           
        
    }

    for (const deleteBtn of deleteBtns) {
        deleteBtn.addEventListener("click", handleClickDelete);
    }