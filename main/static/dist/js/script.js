/*
// Open the Modal
function openModal() {
  document.getElementById("myModal").style.display = "block";
}

// Close the Modal
function closeModal() {
  document.getElementById("myModal").style.display = "none";
}

var slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("demo");
  var captionText = document.getElementById("caption");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
  captionText.innerHTML = dots[slideIndex-1].alt;
}
*/
/* When the user clicks on the button, 
toggle between hiding and showing the dropdown content */
function openhidden(dropdown) {
  el = document.getElementById(dropdown);
  el.style.display = 'block';
}

function openPage(pageName, elmnt) {
  // Hide all elements with class="tabcontent" by default */
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Remove the background color of all tablinks/buttons
  tablinks = document.getElementsByClassName("tablink");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].style.color = "";
    tablinks[i].style.borderBottom = "";
  }

  // Show the specific tab content
  document.getElementById(pageName).style.display = "block";

  // Add the specific color to the button used to open the tab content
  elmnt.style.color = "rgb(29, 161, 242)";
  elmnt.style.borderBottom = "2px solid rgb(29, 161, 242)";
}

// Get the element with id="defaultOpen" and click on it
elmnt = document.getElementById("defaultOpen");
if (elmnt)
  elmnt.click();


/* Set the width of the sidebar to 250px (show it) */
function openDrawer() {
  document.getElementById("drawer").style.width = "70%";
  drawer = document.getElementsByClassName('drawer');
  drawer[0].style.width = '100vw';
  // openhidden("more");
}

/* Set the width of the sidebar to 0 (hide it) */
function closeDrawer() {
  document.getElementById("drawer").style.width = 0;
  drawer.style.width = 0;
  drawer = document.getElementsByClassName('drawer');
  drawer[0].style.opacity = 0;
  drawer[0].style.width = 0;
}

// Close the dropdown if the user clicks outside of it
window.onclick = function (event) {
  if (!event.target.matches(".panel-show")) {
    console.log("I',m working");
    var dropdowns = document.getElementsByClassName("panel");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.style.display) {
        openDropdown.style.display = 'none';
      }
    }
  }

  if (!event.target.matches('.panel-show')) {
    console.log("I'");
    var drawer = document.getElementById("drawer");
    drawer.style.width = 0;
    drawer = document.getElementsByClassName('drawer');
    drawer[0].style.width = 0;

  }

  if (event.target == modal) {
    modal.style.display = "none";
  }
}

// // Close the dropdown if the user clicks outside of it
// window.onclick = function(event) {

// }

// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
// var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal 
// btn.onclick = function() {
//   modal.style.display = "block";
// }

// When the user clicks on <span> (x), close the modal
// span.onclick = function() {
//   modal.style.display = "none";
// }

// // When the user clicks anywhere outside of the modal, close it
// window.onclick = function(event) {

// }

 function max768Func(x) {
   if (x.matches) { // If media query matches
    var el = document.getElementById('context-menu');
    if (el){
      el.classList.add('modal');
      el.classList.remove('context-menu-dropdown');
    }
    //  var collapsibles = document.getElementsByClassName('collapsible')
    //    var i;
    //    for (i=0; i<collapsibles.length; i++){
    //      collapsible = collapsibles[i];
    //      collapsible.classList.remove('drawer-content');
   } 
 }

 function min768Func(x) {
  if (x.matches) { // If media query matches
   var el = document.getElementById('context-menu');
   if (el){
     el.classList.remove('modal');
     el.classList.add('context-menu-dropdown');
   }
   //  var collapsibles = document.getElementsByClassName('collapsible')
   //    var i;
   //    for (i=0; i<collapsibles.length; i++){
   //      collapsible = collapsibles[i];
   //      collapsible.classList.remove('drawer-content');
  } 
}

 var max768 = window.matchMedia("(max-width: 786px)");
 max768Func(max768); // Call listener function at run time
 max768.addListener(max768Func);

 var min768 = window.matchMedia("(min-width: 786px)");
 min768Func(min768); // Call listener function at run time
 min768.addListener(min768Func);