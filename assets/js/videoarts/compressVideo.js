import regeneratorRuntime from "regenerator-runtime";;
import { createFFmpeg, fetchFile } from "@ffmpeg/ffmpeg";
const videoInput = document.getElementById("id_video");
const posterInput = document.getElementById("id_poster");
const thumbnailInput = document.getElementById("id_thumbnail");
const submitDiv = document.querySelector(".upload_submit");
const submitBtn = submitDiv.querySelector("button");
const progress = document.getElementById("progress");
const progressBar = document.getElementById("progress_bar");

let newFile;
let dT = new DataTransfer();
let percent;

const handleSizeValidation = (e) => {
    const { files } = e.target;
    const { size } = files[0];
    const sizeLimit = 10 * 1024 * 1024
    if ( size > sizeLimit ) {
        window.alert("l'immagine si deve essre meno di 10MB") // 대신에 django errer 띄울수 있는지 확인
        e.target.value="";
    }

}

const handleCompress = async (e) => {
    const { files } = e.target;
    const { name : rawVideo, size : rawVideoSize } = files[0];
    const sizeLimit = 1500 * 1024 * 1024 

    if (rawVideoSize > sizeLimit) {
        window.alert("Il video orginale si deve essre meno di 1.5GB")
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
    const ffmpeg = createFFmpeg({ log: true });
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

    window.alert("La compressione video è finita! Ora puoi caricare video. Grazie per la pazienza.")
    submitBtn.innerText = "Carica"
    submitBtn.disabled = false;
    progress.hidden = true;
    submitBtn.style.backgroundColor = "#ca5b4c"
    console.log(videoInput.files[0].size);

}



videoInput.addEventListener("change", handleCompress);
posterInput.addEventListener("change", handleSizeValidation);
thumbnailInput.addEventListener("change", handleSizeValidation);



