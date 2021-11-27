import axios from "axios";

const reviewContainer = document.querySelector(".reviewForm_container");
const InfoContainer = document.querySelector(".detail_movieInfo");
const objType = InfoContainer.dataset.obj

const likeItDiv = document.querySelector(".movie_like_it")
const likeItBtn = document.querySelector(".movie_like_it_btn");
const likeItIco = likeItBtn.querySelector("i");

const handleClickLikeIt = () => {
    if ( objType == "movie" ) {
        const moviePk = reviewContainer.dataset.pk
        let state = likeItDiv.dataset.state
        let handleType = null;
        
        if ( state == "empty" ) {
            handleType = "add"
        }
        else {
            handleType = "remove"
        }

        axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"; 
        axios.defaults.xsrfCookieName = "csrftoken";

        let data = new FormData();

        data.append("handleType", handleType );
    
        axios.post(`/movies/api/${moviePk}/fav/`, data)
        .then(res => { 
            const result = res.data.result
            if ( result == "added" ) {
                likeItIco.className = "fas fa-heart";
                likeItDiv.dataset.state = "filled"
            }
            else {
                likeItIco.className = "far fa-heart";
                likeItDiv.dataset.state = "empty"
            }

        })
        .catch(errors => console.log(errors.response.data));

    
    } else {
        const videoArtPk = reviewContainer.dataset.pk
        let state = likeItDiv.dataset.state
        let handleType = null;
        
        if ( state == "empty" ) {
            handleType = "add"
        }
        else {
            handleType = "remove"
        }

        axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"; 
        axios.defaults.xsrfCookieName = "csrftoken";

        let data = new FormData();

        data.append("handleType", handleType );
    
        axios.post(`/videoarts/api/${videoArtPk}/fav/`, data)
        .then(res => { 
            const result = res.data.result
            if ( result == "added" ) {
                likeItIco.className = "fas fa-heart";
                likeItDiv.dataset.state = "filled"
            }
            else {
                likeItIco.className = "far fa-heart";
                likeItDiv.dataset.state = "empty"
            }

        })
        .catch(errors => console.log(errors.response.data));

    }
}

    


likeItBtn.addEventListener("click", handleClickLikeIt);