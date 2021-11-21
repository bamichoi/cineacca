import axios from "axios"


const reviewContainer = document.querySelector(".reviewForm_container");
const moviePk = reviewContainer.dataset.pk

axios.get(`/api/movies/${moviePk}/view`)
.then(res => { return })
.catch(errors => console.log(errors.response.data));