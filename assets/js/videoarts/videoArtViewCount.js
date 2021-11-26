import axios from "axios"

const reviewContainer = document.querySelector(".reviewForm_container");
const videoArtPk = reviewContainer.dataset.pk

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"; 
axios.defaults.xsrfCookieName = "csrftoken";

let data = new FormData();
 
axios.post(`/videoarts/api/videoarts/${videoArtPk}/view/`, data)
.then(res => { return })
.catch(errors => console.log(errors.response.data));