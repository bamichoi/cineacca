import regeneratorRuntime from "regenerator-runtime";;
import { createFFmpeg, fetchFile } from "@ffmpeg/ffmpeg";
const videoInput = document.getElementById("id_video");

let newFile
let dT = new DataTransfer();

const handleCompress = async (e) => {

    const { files } = e.target
    const { name : rawVideo } = files[0]
    const videoName = rawVideo.slice(0, -4)
    const time = new Date().getTime();
    const newVideoName = videoName + time + ""
    console.log(newVideoName)
    const ffmpeg = createFFmpeg({ log: true });
    await ffmpeg.load();
    

    ffmpeg.FS('writeFile', rawVideo, await fetchFile(files[0]));
    await ffmpeg.run('-i', rawVideo, '-vcodec', 'h264', '-crf', '28', '-acodec', 'mp3', 'output.mp4');
    
    const data = ffmpeg.FS('readFile', 'output.mp4');
    console.log(data)    

    newFile = new File([data], newVideoName, {type:"video/mp4", lastModified:new Date().getTime()});

    dT.items.add(newFile);
    videoInput.files = dT.files
    console.log(videoInput.files)

}



videoInput.addEventListener("change", handleCompress)




