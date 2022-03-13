import regeneratorRuntime from "regenerator-runtime";

const copyBtn = document.querySelector(".copy_link_btn");

const handleClickCopyBtn = async (event) => {
  const currentUrl = window.location.href;
  await navigator.clipboard.writeText(currentUrl);
  alert("l'URL di questo video è copiato!");
};
copyBtn.addEventListener("click", handleClickCopyBtn);
