function addClass( element, classname ) {
if (element.classList)
  element.classList.add(classname);
else
  element.className += ' ' + classname;
}

function removeClass( classname, element ) {
    var cn = element.className;
    var rxp = new RegExp( "\\s?\\b"+classname+"\\b", "g" );
    cn = cn.replace( rxp, '' );
    element.className = cn;
}

var progressBarEl = document.getElementById("progress-bar");
var controlsPlayEl = document.getElementById("controls-play");

function play() {
  // addClass(progressBarEl, "play");
  // addClass(controlsPlayEl, "play");
togglePause()

}

function togglePause() {
console.log(controlsPlayEl.classList.contains ("play"))
    console.log(controlsPlayEl.classList[1])
   if (controlsPlayEl.classList[1] =="play")
   {controlsPlayEl.classList.remove("play")
   console.log (controlsPlayEl.classList[1])
   }
    else {controlsPlayEl.classList.add("play")
    console.log("here")}
}
var slider = document.getElementById("myRange");
var output = document.getElementById("demo");
output.innerHTML = slider.value;
slider.oninput = function() {
  output.innerHTML = this.value;
}