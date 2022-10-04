var input = document.querySelector(".pics")
$(document).ready(function () {

  $(".picer").click(function () {
    $(".pics").click();
});

input.addEventListener("change", function (){
    let folder = this.files[0];
    if (folder.type == "image/png" | folder.type == "image/jpeg") {
    let fileReader = new FileReader();
    fileReader.onload = ()=>{
      let fileURL = fileReader.result;
      pics = fileURL
      pict = document.querySelector(".picer")
      pict.src = fileURL
    };
    fileReader.readAsDataURL(folder);
    }})
 
})

var lon = document.querySelector(".lon")
var lat = document.querySelector(".lat")
var check = document.querySelector(".check")


function getLocation(){
  if (navigator.geolocation){
    navigator.geolocation.watchPosition(showPosition, showError);
  }
  else{
    Swal.fire(
      'Error',
      "Geolocation is not supported by this browser",
      'warning'
     )
     return false;
  }
}

function showPosition(position){
  console.log(position.coords.latitude)
  console.log(position.coords.longitude)
  lat.value = position.coords.latitude
  lon.value = position.coords.longitude

}

function showError(error){
  switch(error.code){
    case error.PERMISSION_DENIED:
      Swal.fire(
        'Error',
        "Unable to get your location because you denied request.",
        'warning'
       )
      break;
    case error.TIMEOUT:
      Swal.fire(
        'Error',
        "Unable to get your location because request time out.",
        'warning'
       )
      break;
    case error.UNKNOWN_ERROR:
      Swal.fire(
        'Error',
        "Unable to get your location because of an unknown error.",
        'warning'
       )
      break;
  }
  check.checked = false;
  return false;
}