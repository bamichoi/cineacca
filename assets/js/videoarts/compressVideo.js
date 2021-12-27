import regeneratorRuntime from "regenerator-runtime";;
import { createFFmpeg, fetchFile } from "@ffmpeg/ffmpeg";
const videoInput = document.getElementById("id_video");
const submitDiv = document.querySelector(".upload_submit");
const submitBtn = submitDiv.querySelector("button");
const progress = document.getElementById("progress");
const progressBar = document.getElementById("progress_bar");

let newFile;
let dT = new DataTransfer();
let percent;

const handleCompress = async (e) => {
    const { files } = e.target;
    const { name : rawVideo, size : rawVideoSize } = files[0];
    const sizeLimit = 100 * 1024 * 1024
    console.log(files, files.length) 

    if (files.length > 1) {
           console.log(files.length)
    }
    if (rawVideoSize > sizeLimit) {
        window.alert("Il video orginale si deve essre meno di 1GB")
        videoInput.value="";
        return
    } 
    
    window.alert(
    "Ora inizia la compresseione video. A seconda dell'ambiente e delle dimesioni del file, potrebbe volerci parecchio tempo. Si prega di evitare di fare un altro lavoro il più possibile. Non appena è finito ti faremo sapre. Si prega di attendere fino al termine del lavoro.")
    
    submitBtn.disabled = true;
    progress.hidden = false
    submitBtn.style.backgroundColor = "#ced6e0"

    const videoName = rawVideo.slice(0, -4);
    const time = new Date().getTime();
    const newVideoName = videoName + time + "";
    console.log(newVideoName)
    const ffmpeg = createFFmpeg({ log: false });
    await ffmpeg.load();
    

    ffmpeg.FS('writeFile', rawVideo, await fetchFile(files[0]));

    ffmpeg.setProgress(({ ratio }) => {
        percent = Math.floor(ratio * 100)
        progressBar.style.width = `${percent}%`
        submitBtn.innerText = `Compressing... ${percent}%`
      });

    await ffmpeg.run('-i', rawVideo, '-vcodec', 'h264', '-crf', '28', '-acodec', 'mp3', 'output.mp4');
    
    const data = ffmpeg.FS('readFile', 'output.mp4'); 

    newFile = new File([data], newVideoName, {type:"video/mp4", lastModified:new Date().getTime()});

    if (dT.items.length > 0 ) {
        dT.items.clear()
    }
    dT.items.add(newFile);
    videoInput.files = dT.files
    console.log(dT.items)

    window.alert("La compressione video è finita! Ora puoi caricare video. Grazie per la pazienza.")
    console.log(files, files.length) 
    submitBtn.innerText = "Carica"
    submitBtn.disabled = false;
    progress.hidden = true;
    submitBtn.style.backgroundColor = "#ca5b4c"
    

}



videoInput.addEventListener("change", handleCompress)




