class Cinta {
  float x = width/2;
  float y = height/2;
  String teks = "AKU";
  color warna_label = color(100, 200, 0);

  void tampilkan() {
    heart.resize(100, 0);
    imageMode(CENTER);
    image(heart, x, y);
  }
  
  void label() {
    textSize(30);
    fill(warna_label);
    text(teks, mouseX, mouseY);
    if (mouseX < width/2) {
      teks = "AKU";
      warna_label = color(100, 200, 0);
    } else if (mouseX > width/2) {
      warna_label = color(200, 200, 10);
      teks = "KAMU";
    }
  }
  
  void hover() {
    if(mouseX > x - heart.width/2 && mouseX < x + heart.width/2) {
      if(mouseY > y - heart.height/2 && mouseY < y + heart.height/2) {
        tampilkan();
        warna_label = color(255);
        teks = "KITA";
      }
    }
  }
}
