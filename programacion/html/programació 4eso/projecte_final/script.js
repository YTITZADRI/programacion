var carpeta = "Gen_1";
var images = ["001.png", "002.png"];
images.forEach(function(img) {
  var image = new Image();
  image.src = carpeta + "/" + img;
  image.onerror = error;
});