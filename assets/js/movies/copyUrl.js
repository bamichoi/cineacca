const copyBtn = document.querySelector(".copy_link_btn");

const handleClickCopyBtn = (event) => {
    const currentUrl = window.location.href
    navigator.clipboard.writeText(currentUrl)
    alert("l'URL di questo video è copiato!")
}
copyBtn.addEventListener("click", handleClickCopyBtn)