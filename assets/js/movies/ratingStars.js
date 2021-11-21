const rateInput = document.getElementById("review_rate");
const fullStars = document.querySelector(".full_stars")
const emptyStars = document.getElementsByClassName("empty_stars")
const score = document.getElementById("score")

const handleOninput = (event) => {
    const { value } = event.target
    const convertValue = value * 20 + "%"
    fullStars.style.width = convertValue

    score.innerText = value.includes(".") ? `"${value}"` : `"${value}.0"`
}
    
rateInput.addEventListener("input", handleOninput)