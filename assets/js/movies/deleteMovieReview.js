import axios from "axios";

const deleteBtns = document.getElementsByClassName("delete");

function handleClickDelete(event) {
  event.preventDefault();
  const deleteBtn = event.target;
  const pk = deleteBtn.value;
  const review = document.getElementById(`${pk}`);
  const object_type = "movie";
  if (confirm("Vuoi veramente eliminare questo review?")) {
    review.hidden = true;

    let data = new FormData();

    data.append("pk", pk);
    data.append("object_type", object_type);

    axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
    axios.defaults.xsrfCookieName = "csrftoken";

    axios
      .post("/reviews/api/delete/", data)
      .then((res) => alert("Il review è emliminato!"))
      .catch((errors) => console.log(errors.response.data));
  }
}

for (const deleteBtn of deleteBtns) {
  deleteBtn.addEventListener("click", handleClickDelete);
}
