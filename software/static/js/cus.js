var input = document.querySelector(".fil")
$(document).ready(function () {

  $(".imgs").click(function () {
    $(".fil").click();
});

input.addEventListener("change", function (){
    let folder = this.files[0];
    if (folder.type == "image/png" | folder.type == "image/jpeg") {
    let fileReader = new FileReader();
    fileReader.onload = ()=>{
      let fileURL = fileReader.result;
      pict = document.querySelector(".imer")
      pict.src = fileURL
    };
    fileReader.readAsDataURL(folder);
    }})
 
})