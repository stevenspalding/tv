// url: 172.16.88.88
// name: s19_telescope

vidlink = document.getElementById("vidlink");
cats = vidlink.children;
out = [];

for (var i = 0; i < cats.length; i++) {
  category = cats[i].className;
  ch = cats[i].firstChild;
  url = ch.dataset.link;
  img = ch.firstChild.src;
  title = img.split("/").slice(-1)[0];
  title = title.replace(".jpg", "").replace(".jpeg", "").replace(".png", "");
  entry = {
    title: title,
    logo: img,
    url: url,
    category: category,
  };
  out.push(entry);
}
out;
