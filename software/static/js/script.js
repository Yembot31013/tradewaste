// Set the date we're counting down to
years = document.querySelector(".year");
var yearDate = new Date();
var year = yearDate.getFullYear();
years.innerHTML = year

var countDownDate = $('input[name=time]').val();

var countDownDate = countDownDate * 1000

// Update the count down every 1 second
var x = setInterval(function () {
  // Get todays date and time
  var now = new Date().getTime();

  // Find the distance between now an the count down date
  var distance = countDownDate - now;

// Time calculations for days, hours, minutes and seconds
var days = Math.floor(distance / (1000 * 60 * 60 * 24));
var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
var seconds = Math.floor((distance % (1000 * 60)) / 1000);

// Display the result in the element with id="demo"
document.getElementById('time-counter').innerHTML =
  days + 'd ' + hours + 'h ' + minutes + 'm ' + seconds + 's ';

// If the count down is finished, write some text
if (distance < 0) {
  clearInterval(x);
  document.getElementById('time-counter').innerHTML = 'Started';
  var token = $('input[name=csrfmiddlewaretoken]').val();
  var zoom_id = $('input[name=zoom_id]').val();
  var course_id = $('input[name=course_id]').val();
  console.log("token", token);
  console.log("zoom_id", zoom_id);
  console.log("course_id", course_id);
  $.ajax({
  method: "POST",
  url: "",
  data: {
  'zoom_id': zoom_id,
  'csrfmiddlewaretoken': token,
  'course_id': course_id,
},
success: function (response) {
  if (response["status"] == 'live'){
    zoom_id = response["id"]
    window.location.href = '/join_live/'+zoom_id+'/'
  }
  else{
    alertify.set("notifier", "position", "top-right");
    alertify.success("live class has started, upgrade your bundle so that you can attend live class");
  }
},
error: function (e) {
  console.log(e)
}
})
    }
  }, 1000);