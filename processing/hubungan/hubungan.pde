PImage heart;
Cinta cinta;
void setup() {
  size(500, 400);
  
  heart = loadImage("purple-heart.png");
  
  cinta = new Cinta();
}

void draw() {
  background(0);  
  //cinta.tampilkan();
  cinta.hover();
  cinta.label();
}
