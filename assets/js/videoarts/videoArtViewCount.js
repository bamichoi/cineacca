import axios from "axios"

 const reviewContainer = document.querySelector(".reviewForm_container");
 const videoArtPk = reviewContainer.dataset.pk

 axios.get(`/api/movies/${videoArtPk}/view`)
 .then(res => { return })
 .catch(errors => console.log(errors.response.data));