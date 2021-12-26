import regeneratorRuntime from "regenerator-runtime";;
import { createFFmpeg, fetchFile } from "@ffmpeg/ffmpeg";
const videoInput = document.getElementById("id_video");
const submitDiv = document.querySelector(".upload_submit");
const submitBtn = submitDiv.querySelector("button");

let newFile;
let dT = new DataTransfer();

const handleCompress = async (e) => {
    window.alert(
    "Ora inizia la compresseione video. A seconda dell'ambiente e delle dimesioni del file, potrebbe volerci parecchio tempo. Si prega di evitare di fare un altro lavoro il più possibile. Non appena è finito ti faremo sapre. Si prega di attendere fino al termine del lavoro.")
    submitBtn.innerText = "Compressing..."
    submitBtn.disabled = true;
    submitBtn.style.backgroundColor = "#ced6e0"

    const { files } = e.target;
    const { name : rawVideo } = files[0];
    const videoName = rawVideo.slice(0, -4);
    const time = new Date().getTime();
    const newVideoName = videoName + time + "";
    console.log(newVideoName);
    const ffmpeg = createFFmpeg({ log: true });
    await ffmpeg.load();
    

    ffmpeg.FS('writeFile', rawVideo, await fetchFile(files[0]));
    await ffmpeg.run('-i', rawVideo, '-vcodec', 'h264', '-crf', '28', '-acodec', 'mp3', 'output.mp4');
    
    const data = ffmpeg.FS('readFile', 'output.mp4'); 

    newFile = new File([data], newVideoName, {type:"video/mp4", lastModified:new Date().getTime()});

    dT.items.add(newFile);
    videoInput.files = dT.files

    window.alert("La compressione video è finita! Ora puoi caricare video. Grazie per la pazienza.")
    submitBtn.innerText = "Carica"
    submitBtn.disabled = false;
    submitBtn.style.backgroundColor = "#ca5b4c"
    

}



videoInput.addEventListener("change", handleCompress)




